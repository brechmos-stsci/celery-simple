import numpy as np

import time
from collections import OrderedDict
import itertools
import logging
from celery import group

from celery_conf import app
from .smoother import calculate


FORMAT = '%(levelname)-8s %(asctime)-15s %(name)-10s %(funcName)-10s %(lineno)-4d %(message)s'
logging.basicConfig(format=FORMAT)
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)


def chunks(l, k):
    n = len(l)
    return [l[i * (n // k) + min(i, n % k):(i+1) * (n // k) + min(i+1, n % k)] for i in range(k)]


def calculate_celery(images):
    """
    This function will queue up all the jobs and run them using celery.
    """

    # Queue up and run
    job = group([
        calculate_task.s(tt) for tt in chunks(images, 3)
    ])
    result = job.apply_async()

    # Display progress -- completely unneccesary,
    # only useful for checking state of completion
    counts = OrderedDict({x.id: 0 for x in result.children})
    while not result.ready():
        time.sleep(0.1)
        for x in result.children:
            if (x.state == 'PROGRESS' and hasattr(x, 'info') and
                    'progress' in x.info):
                counts[x.id] = x.info['progress']

        states_complete = [int(v) for k, v in counts.items()]
        print('\rCalculating fingerprints: {} {:.1f}%'.format(
            states_complete, sum(states_complete)/len(images)*100), end='')

    # Get the results (is a list of lists so need to compress them)
    # This is needed.
    r = result.get()
    return list(itertools.chain(*r))


@app.task
def calculate_task(images):
    """
    This is the task/function that gets run from the queue.
    """
    log.debug('app.current_task {}'.format(app.current_task))

    # The second parameter allows state information to be passed back
    return calculate(images, task=app.current_task)
