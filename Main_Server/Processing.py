import cv2
import os
import numpy as np

class Processing:
    def toHSV(img):
        return cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    def blurAndContour(self, imgHSV, blurType):
        if blurType == 'median':
            blurred = cv2.medianBlur(imgHSV, 15)
        #----------v-v-v-v-v-v-v-v-v-v-v-v-v-v-v-v-v-v-v-v----------#
        contours = cv2.findContours(blurred, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[0]
        if len(contours) == 0:
            print('blurAndContours // ERROR: No Contours Found')
            return None
        #----------^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^----------#
        retImage = cv2.drawContours(blurred, contours, -1, (0, 255, 0), 3)
        retTuple = (retImage, blurred, contours)
        return retTuple

    def threshAndContour(self, imgHSV, threshLow, threshHigh):
        threshed = cv2.inRange(imgHSV, threshLow, threshHigh)
        #----------v-v-v-v-v-v-v-v-v-v-v-v-v-v-v-v-v-v-v-v----------#
        contours = cv2.findContours(threshed, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[0]
        if len(contours)==0:
            print('threshAndContours // ERROR: No Contours Found')
            return None
        #----------^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^----------#
        retImage = cv2.drawContours(threshed, contours, -1, (0, 255, 0), 3)
        retTuple = (retImage, threshed, contours)
        return retTuple

    def bothAndContours(self, img, threshLow, threshHigh, blurType):
        dud1, threshed = self.threshAndContour(img, threshLow, threshHigh)
        dud2, BAT = self.blurAndContours(threshed, blurType)
        #----------v-v-v-v-v-v-v-v-v-v-v-v-v-v-v-v-v-v-v-v----------#
        contours = cv2.drawContours(BAT, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[0]
        if len(contours) == 0:
            print('bothAndContours // ERROR: No Contours Found')
            return None
        #----------^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^----------#
        wContours = cv2.drawContours(BAT, contours, -1, (0, 255, 0), 3)
        retTuple = (wContours, BAT, contours)
        return retTuple

    def contour(self, imgHSV):
        #----------v-v-v-v-v-v-v-v-v-v-v-v-v-v-v-v-v-v-v-v----------#
        contours = cv2.drawContours(imgHSV, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[0]
        if len(contours) == 0:
            print('contours // ERROR: No Contours Found')
            return None
        #----------^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^----------#
        wContours = cv2.drawContours(imgHSV, contours, -1, (0, 255, 0), 3)
        return tuple(wContours, contours)

    def filterRectBasic(self, imgHSV, Rw, Rh, func): #"blurAC", "threshAC", "bothAC", else
        locatedTargets = []
        targetRatio = Rw/Rh
        
        if func == 'blurAC':
            res, blur, contours = self.blurAndContour(imgHSV, 'median')
            width, height = cv2.GetSize(res)
            blank = np.zeros((width, height), np.uint8)
            try:
                for c in contours:
                    x, y, w, h = cv2.boundingRect()
                    ratio = w/h
                    rectRatio = Rw/Rh
                    if 0.2 < ratio/rectRatio < 1.8:
                        locatedTargets.append(c)
                for t in locatedTargets:
                    blank = cv2.drawContours(blank, t, -1, (0, 255, 0), 3)
                return blank
            except:
                return None
        #----------^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^----------#
        elif func == 'threshAC':
            res, thresh, contours = self.threshAndContour(imgHSV, np.array, np.array)
            width, height = cv2.GetSize(res)
            blank = np.zeros((width, height), np.uint8)
            try:
                for c in contours:
                    x, y, w, h = cv2.boundingRect()
                    ratio = w/h
                    rectRatio = Rw/Rh
                    if 0.2 < ratio/rectRatio < 1.8:
                        locatedTargets.append(c)
                for t in locatedTargets:
                    blank = cv2.drawContours(blank, t, -1, (0, 255, 0), 3)
                return blank
            except:
                return None
        #----------^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^----------#
        elif func == 'bothAC':
            res, both, contours = self.bothAndContours(imgHSV, np.array([100, 120, 190]), np.array([110, 160, 230]), 'median')
            width, height = cv2.GetSize(res)
            blank = np.zeros((width, height), np.uint8)
            try:
                for c in contours:
                    x, y, w, h = cv2.boundingRect()
                    ratio = w/h
                    rectRatio = Rw/Rh
                    if 0.2 < ratio/rectRatio < 1.8:
                        locatedTargets.append(c)
                for t in locatedTargets:
                    blank = cv2.drawContours(blank, t, -1, (0, 255, 0), 3)
                return blank
            except:
                return None
        #----------^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^----------#
        else:
            res, contours = self.contours(imgHSV)
            width, height = cv2.GetSize(res)
            blank = np.zeros((width, height), np.uint8)
            try:
                for c in contours:
                    x, y, w, h = cv2.boundingRect()
                    ratio = w/h
                    rectRatio = Rw/Rh
                    if 0.2 < ratio/rectRatio < 1.8:
                        locatedTargets.append(c)
                for t in locatedTargets:
                    blank = cv2.drawContours(blank, t, -1, (0, 255, 0), 3)
                return blank
            except:
                return None
            
