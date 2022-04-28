import cv2
import numpy as np


def apply_clahe(x):
    clahe = cv2.createCLAHE(clipLimit=2, tileGridSize=(4, 4))
    x[:, :, 0] = clahe.apply(x[:, :, 0])
    x[:, :, 1] = x[:, :, 0]
    x[:, :, 2] = x[:, :, 0]
    return x


def get_img_as_input(img_path, clahe_apply=False, print_img=False):
    W = H = 256
    x = cv2.imread(img_path, cv2.IMREAD_COLOR)
    resized_x = cv2.resize(x, (W, H))
    ori_x = resized_x

    if print_img:
        cv2.imshow("Resized Input CXR Image", ori_x)
    if clahe_apply:
        x = apply_clahe(resized_x)

    x = resized_x / 255.0
    x = x.astype(np.float32)
    x = np.expand_dims(x, axis=0)
    return (resized_x, x)
