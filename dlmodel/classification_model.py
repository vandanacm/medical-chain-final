import tensorflow as tf
import cv2
import numpy as np


def load_classification_model():
    global classification_model
    classification_model = tf.keras.models.load_model("model_incep_kaggle.h5")


def classify(seg_img):
    # remove after replacing .h5 file
    H_incep_kaggle = W_incep_kaggle = 224
    seg_img = cv2.resize(seg_img, (W_incep_kaggle, H_incep_kaggle))
    seg_img = seg_img.reshape(1, W_incep_kaggle, H_incep_kaggle, 3)

    label_pred = classification_model.predict(seg_img) > 0.5
    return np.squeeze(label_pred)
