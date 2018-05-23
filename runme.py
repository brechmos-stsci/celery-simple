import numpy as np
from image_processing.celery_smoother import calculate_celery

# This is the main code to run

#
# Create some random images to send to the processing machine
#
images = [np.random.random((256, 256)) for x in range(10)]

smoothed_images = calculate_celery(images)
