import numpy as np
import logging


FORMAT = '%(levelname)-8s %(asctime)-15s %(name)-10s %(funcName)-10s %(lineno)-4d %(message)s'
logging.basicConfig(format=FORMAT)
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)


def calculate(images, task=None):
    """
    Calculate the fingerprint from a list of data.  The data
    must be of the form
         [ {'uuid': <somtehing>, 'location': <somewhere>, 'meta': {<meta data} }... ]
    """
    log.info('')

    # Now run through each datum and calculate the fingerprint
    images_return = []
    for ii, image in enumerate(images):

        # Update the progress if we are using the task version of this.
        if task is not None:
            task.update_state(state='PROGRESS', meta={'progress': ii})

        # Calculate the predictions
        log.debug('calcuating on {}'.format(image))
        try:
            image_out = image
        except Exception as e:
            log.error('Problem calculating predictions, {}'.format(e))

        # Load up the return list.
        images_return.append(image_out)

    return images_return
