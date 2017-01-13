import cv2
import numpy as np
import threading
from GlobalData import HSV_lowThresh
from GlobalData import HSV_highThresh

class Filtering(threading.Thread):
    def __init__(self, img):
        threading.Thread.__init__(self)
        self.original_frame = img
        self.hsvImg = None
        self.FilteredLow = None
        self.FilteredHigh = None
        self.FilteredComplete= None
        self.Filtered = None

    def run(self):
        global HSV_lowThresh
        global HSV_highThresh

        cam = cv2.VideoCapture(0)
        _, f = cam.read()

        self.threshHSV(self.toHSV(f), HSV_lowThresh, HSV_highThresh)


    def toHSV(self, frame):                                             #converts an image to HSV
        return cv2.cvtColor(self.original_frame, cv2.COLOR_BGR2HSV)


    def ThreshHSVCombined(self, frame,lowThresh, highThresh):
        self.FilteredLow = cv2.inRange(self.hsvIMG, np.array(lowThresh[0]), np.array(lowThresh[1]))
        self.FilteredHigh = cv2.inRange(self.hsvIMG, np.array(highThresh[0]), np.array(highThresh[1]))
        self.Filtered = cv2.add(self.FilteredLow, self.FilteredHigh)

    def threshHSV(self, frame, low_thresh, high_thresh):#lowThresh & highThresh are NP ARRAYS, threshs the hs image
        return cv2.inRange(frame, low_thresh, high_thresh)

    def findContours(self, frame):
        __a, contours, hierarchy = cv2.findContours(threshed, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        empty = np.zeros((threshed.shape[0], threshed.shape[1], 3), np.uint8)
        wContours = cv2.drawContours(empty, contours, -1, (0, 255, 0), 3)



if __name__ == '__main__':
    CapWeb = cv2.VideoCapture(0)
    #while True:
    _, frame = CapWeb.read()
    CapWeb.release()
    cv2.imshow("frame", frame)
    c1 = Filtering(frame)
    c1.toHSV()
    threshed = c1.threshHSV(np.array([108, 117, 126]), np.array([180, 203, 255]))
    median = cv2.medianBlur(threshed, 15)
    cv2.imshow("median", median)
    __a, contours, hierarchy = cv2.findContours(threshed,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    empty = np.zeros((threshed.shape[0],threshed.shape[1],3), np.uint8)
    wContours = cv2.drawContours(empty, contours, -1, (0,255,0), 3)
    cv2.imshow("w/ contours", wContours)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    CapWeb.release()
