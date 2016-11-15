import numpy
import cv2
import FilterHSV as fHSV

while (True):
    frame = cv2.VideoCapture(-1)

    frame.set(3, 320)
    frame.set(4, 240)

    #cv2.namedWindow("Image")
    #cv2.imshow("Image")