from metrics import *
from load_img import *
from segmentation_model import *
from classification_model import *
# from pdf_maker import *


def predict_covid(parameters, img_path):
    H = W = 256
    classification_model = seg_model = None
    # load_seg_model()
    # load_classification_model()
    # resized_img, img_inp = get_img_as_input(img_path, print_img=False, clahe_apply=parameters['low_contrast'])
    # mask_pred = predict_from_unet(img_inp, print_pred_mask=False)
    # seg_img = get_seg_img(mask_pred, resized_img, print_img=False)
    # label_pred = classify(seg_img)
    # cv2.waitKey(0)
    return True
    # return create_pdf(parameters, label_pred)
