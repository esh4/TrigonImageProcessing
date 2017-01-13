import cv2
import numpy as np

class Filtering:
    def __init__(self, img):
        self.orgIMG = img
        self.hsvIMG = None
        self.FilteredLow = None
        self.FilteredHigh = None
        self.FilteredComplete= None
        self.Filtered = None

    def ToHSV(self):#converts an image to HSV
        self.hsvIMG = cv2.cvtColor(self.orgIMG, cv2.COLOR_BGR2HSV)
        return self.hsvIMG

    def ThreshHSVCombined(self, lowThresh, highThresh):
        self.FilteredLow = cv2.inRange(self.hsvIMG, np.array(lowThresh[0]), np.array(lowThresh[1]))
        self.FilteredHigh = cv2.inRange(self.hsvIMG, np.array(highThresh[0]), np.array(highThresh[1]))
        self.Filtered = cv2.add(self.FilteredLow, self.FilteredHigh)

    def ThreshHSV(self, lowThresh, highThresh):#lowThresh & highThresh are NP ARRAYS, threshs the hs image
        self.Filtered = cv2.inRange(self.hsvIMG, lowThresh, highThresh)
        return self.Filtered



if __name__ == '__main__':
    CapWeb = cv2.VideoCapture(1)
    while True:
        _, frame = CapWeb.read()
        cv2.imshow("frame", frame)
        c1 = Filtering(frame)
        c1.ToHSV()
        threshed = c1.ThreshHSV(np.array([4, 170, 170]), np.array([12, 255, 255]))
        median = cv2.medianBlur(threshed, 15)
        cv2.imshow("median", median)
        __a, contours, hierarchy = cv2.findContours(threshed,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
        empty = np.zeros((threshed.shape[0],threshed.shape[1],3), np.uint8)
        wContours = cv2.drawContours(empty, contours, -1, (0,255,0), 3)
        cv2.imshow("w/ contours", wContours)
        if cv2.waitKey(5) &0xFF == 27:
            break
    cv2.destroyAllWindows()
    CapWeb.release()
