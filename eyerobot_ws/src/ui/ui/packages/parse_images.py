import os

import cv2
import numpy as np


def parse_images():
    input_path = "/app/user_input/"
    output_path = "/app/user_images/"
    os.makedirs(output_path, exist_ok=True)
    for filename in os.listdir(input_path):
        with open(os.path.join(input_path, filename)) as f:
            images = np.fromfile(f, dtype=np.uint16)
            images = images.reshape(336, 200, 200)
            for i, image in enumerate(images):
                cv2.imwrite(os.path.join(output_path, filename + "_" + str(i).zfill(3) + ".png"), image)
