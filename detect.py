import cv2
import cvlib as cv

img = cv2.imread("images/good_face.jpg")
boxes, labels, conf = cv.detect_common_objects(img, model="yolov4")

print(labels, boxes, conf)
