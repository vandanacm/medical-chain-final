import tensorflow as tf
from metrics import *
import cv2


def load_seg_model():
    global seg_model
    with tf.keras.utils.CustomObjectScope(
        {"iou": iou, "dice_coef": dice_coef, "dice_loss": dice_loss}
    ):
        seg_model = tf.keras.models.load_model("model_unet_v2.h5")


def imporve_mask(y_pred):
    gray = np.squeeze(y_pred)

    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (10, 10))
    gray = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)

    img = cv2.pyrDown(gray)
    _, threshed = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(threshed, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    contours = sorted(contours, key=cv2.contourArea, reverse=True)
    cmax2 = cmax1 = contours[0]
    width, height = gray.shape

    img = np.zeros([width, height, 3], dtype=np.uint8)
    if len(contours) > 1:
        cmax2 = contours[1]
        cv2.fillPoly(img, pts=[cmax1, cmax2], color=(255, 255, 255))
    else:
        cv2.fillPoly(img, pts=[cmax1], color=(255, 255, 255))

    img = cv2.GaussianBlur(img, (15, 15), 0)
    img = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)[1]

    return img


def predict_from_unet(x, print_pred_mask=False):
    y_pred = seg_model.predict(x)[0] > 0.5
    y_pred = y_pred.astype(np.uint8)
    y_pred *= 255
    y_pred = imporve_mask(y_pred)
    if print_pred_mask:
        cv2.imshow("y_pred", y_pred)
    # y_pred = np.concatenate([y_pred, y_pred, y_pred], axis=-1)
    y_pred = tf.cast(y_pred, tf.uint8)
    return y_pred


def get_seg_img(mask_pred, resized_img, print_img=False):
    seg_img = np.bitwise_and(mask_pred, resized_img)
    if print_img:
        cv2.imshow("Segmented Image", seg_img)
    return seg_img
