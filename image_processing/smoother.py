import numpy as np
import logging


FORMAT = '%(levelname)-8s %(asctime)-15s %(name)-10s %(funcName)-10s %(lineno)-4d %(message)s'
logging.basicConfig(format=FORMAT)
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

#
#  This is horrible slow code. And it is supposed to be...
#


def calculate(images, task=None):
    """
    """
    log.info('')

    #
    # Now run through each datum and calculate the fingerprint
    #

    images_return = []
    for ii, image in enumerate(images):
        log.info('Calculating for image {}/{}'.format(ii, len(images)))

        #
        # Update the progress if we are using the task version of this.
        #

        if task is not None:
            task.update_state(state='PROGRESS', meta={'progress': ii})

        #
        #  GACK, wow, what a horribly slow implementation
        #  ah, yeah, that's the point :)
        #  How could this be sped up, let me count thy ways...
        #

        image_out = np.zeros(image.shape)

        for row in range(image.shape[0]):
            for col in range(image.shape[1]):
                rs = max(0, row-1)
                re = min(image.shape[0]-1, row+1)
                cs = max(0, col-1)
                ce = min(image.shape[1]-1, col+1)
                image_out[row, col] = np.mean(image[rs:re, cs:ce])

        #
        # Load up the return list.
        #

        images_return.append(image_out)

    return images_return
