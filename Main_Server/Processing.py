import cv2
import os
import numpy as np

class Processing:
    def toHSV(self, img):
        return cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    '''def blurAndContour(self, imgHSV, blurType):
        if blurType == 'median':
            blurred = cv2.medianBlur(imgHSV, 15)
        #----------v-v-v-v-v-v-v-v-v-v-v-v-v-v-v-v-v-v-v-v----------#
        contours = cv2.findContours(blurred, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[0]
        if len(contours) == 0:
            print('blurAndContours // ERROR: No Contours Found')
            return None
        #----------^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^----------#
        contours = np.array(contours).reshape((-1, 1, 2)).astype(np.int32)
        retImage = cv2.drawContours(blurred, [contours], -1, (0, 255, 0), 3)
        retTuple = (retImage, blurred, contours)
        return retTuple
    '''
    def blurAndContour(self, imgHSV, blurType):
        #if blurType == 'median':
        blurred = cv2.medianBlur(imgHSV, 15)                                            #median blurs he image
        _, contours, _ = cv2.findContours(blurred, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)    #finds the contuours

        if len(contours) == 0:          #checks that contours exsist
            print('blurAndContours // ERROR: No Contours Found')
            return None

        returnImage = cv2.drawContours(blurred, contours, -1, 255, 3)             #draws the contours on the image
        returnTuple = (returnImage, blurred, contours)                                      #returns - retImage, the blurred image with contours on it; the blurred image; the contours themselves
        return returnTuple

    '''def threshAndContour(self, imgHSV, threshLow, threshHigh):
        threshed = cv2.inRange(imgHSV, threshLow, threshHigh)
        #----------v-v-v-v-v-v-v-v-v-v-v-v-v-v-v-v-v-v-v-v----------#
        contours = cv2.findContours(threshed, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)#[0]
        print(len(contours))
        input()
        if len(contours) == 0:
            print('threshAndContours // ERROR: No Contours Found')
            return None
        #----------^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^----------#
        contours = np.array(contours).astype(np.int32)
        retImage = cv2.drawContours(threshed, contours, -1, (0, 255, 0), 3)
        retTuple = (retImage, threshed, contours)
        return retTuple
    '''

    def threshAndContour(self, imgHSV, threshLow, threshHigh):
        blurred_image = cv2.medianBlur(imgHSV, 15)
        threshed = cv2.inRange(blurred_image, np.array(threshLow), np.array(threshHigh))                #threshholds he image
        _, contours, _ = cv2.findContours(threshed, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)       #finds the contuour
        print("cnts", len(contours))

        if len(contours) == 0:      #checks that contours exsist
            print('threshAndContours // ERROR: No Contours Found')
            return None

        returnImage = cv2.drawContours(threshed, contours, -1, 255, 3)        #draws the contours on the image
        returnTuple = (returnImage, threshed, contours)                                 #returns - retImage, the threshed image with contours on it; the threshed image; the contours themselves
        return returnImage, threshed, contours
    '''
    def bothAndContours(self, img, threshLow, threshHigh, blurType):
        dud, threshed, dud = self.threshAndContour(self, img, threshLow, threshHigh)
        dud, blurred_and_threshed, contours = self.blurAndContour(self, threshed, blurType)

        withContours = cv2.drawContours(blurred_and_threshed, [contours], -1, (0, 255, 0), 3)
        retTuple = (withContours, blurred_and_threshed, contours)
        return retTuple
    '''

    def bothAndContours(self, img, threshLow, threshHigh, blurType):
        result_image, threshed_image, contours = self.threshAndContour(self, img, threshLow, threshHigh)                #gets the threshed image
        #dud, blurred_and_threshed, contours = self.blurAndContour(self, img, blurType)         #gets it'scontours and blurs it
        
        #withContours = cv2.drawContours(threshed_image, contours, -1, (0, 255, 0), 3)       #draws contours on separate image
        withContours = 0
        returnTuple = (withContours, threshed_image, contours)       #returns - withContours, the threshed&blurred image with contours on it; the threshed&blurred; the contours themselves
        return returnTuple

    '''
    def contour(self, imgHSV):
        #----------v-v-v-v-v-v-v-v-v-v-v-v-v-v-v-v-v-v-v-v----------#
        contours = cv2.drawContours(imgHSV, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[0]
        if len(contours) == 0:
            print('contours // ERROR: No Contours Found')
            return None
        #----------^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^----------#
        contours = np.array(contours).reshape((-1, 1, 2)).astype(np.int32)
        wContours = cv2.drawContours(imgHSV, [contours], -1, (0, 255, 0), 3)
        return tuple(wContours, contours)
    '''
    def contour(self, imgHSV):

        contours = cv2.findContours(imgHSV, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[0]          #finds image contours

        if len(contours) == 0:#checks that contours exsist
            print('contours // ERROR: No Contours Found')
            return None

        withContours = cv2.drawContours(imgHSV, contours, -1, (0, 255, 0), 3)                 #draws contours onto the image
        return tuple(withContours, contours)                        #returns the image with contours; the contours themselves

    '''
    def filterRectBasic(self, imgHSV, Rw, Rh, func): #"blurAC", "threshAC", "bothAC", else
        locatedTargets = []
        targetRatio = Rw/Rh
        
        if func == 'blurAC':
            res, blur, contours = self.blurAndContour(self, imgHSV, 'median')
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
                    blank = cv2.drawContours(blank, [t], -1, (0, 255, 0))
                return blank
            except:
                return None
        #----------^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^----------#
        elif func == 'threshAC':
            res, thresh, contours = self.threshAndContour(self, imgHSV, np.array([100, 120, 190]), np.array([110, 160, 230]))
            width, height = res.shape[:2]
            blank = np.zeros((width, height), np.uint8)

            print(len(contours))
            input("")
            for c in contours:
                x, y, w, h = cv2.boundingRect()
                ratio = w/h
                rectRatio = Rw/Rh
                if 0.2 < ratio/rectRatio < 1.8:
                    locatedTargets.append(c)
            for t in locatedTargets:
                blank = cv2.drawContours(blank, [t], -1, (0, 255, 0), 3)
            return blank

        #----------^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^----------#
        elif func == 'bothAC':
            res, both, contours = self.bothAndContours(self, imgHSV, np.array([100, 120, 190]), np.array([110, 160, 230]), 'median')
            width, height = res.shape[:2]
            blank = np.zeros((width, height), np.uint8)

            print(len(contours))
            input("")
            for c in contours:
                x, y, w, h = cv2.boundingRect(c)
                ratio = w/h
                print(ratio / targetRatio)
                if 0.2 < ratio/targetRatio < 1.8:
                    locatedTargets.append(c)
            for t in locatedTargets:
                blank = cv2.drawContours(blank, [t], -1, (0, 255, 0), 3)
                return blank

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

    '''

    def filterRectBasic(self, imgHSV, rectangleWidth, rectangleHeight, function):   #"blurAC"->blurAndConours, "threshAC"->threshAndContours, "bothAC"->bothAndContours, else->contours
        locatedTargets = []                         #blank array he aquired targets' contours
        targetRatio = rectangleWidth/rectangleHeight                                #the ratio of width and height of what we are looking for
        
        if function == 'blurAC':
            result, blur, contours = self.blurAndContour(self, imgHSV, 'median')
            height, width = result.shape[:2]            #gets the image size
            blank = np.zeros((height, width), np.uint8)
            for c in contours:
                x, y, w, h = cv2.boundingRect()         #finds the contour rectangle
                ratio = w/h                             #calculates it's ratio
                if 0.2 < ratio/targetRatio < 1.8:       #is it close enough?
                    locatedTargets.append(c)            #if so, save this contour
            for t in locatedTargets:
                blank = cv2.drawContours(blank, [t], -1, (0, 255, 0))#draws these contours on a blank image
            return blank
            #and again and again for each function

        elif function == 'threshAC':
            result, thresh, contours = self.threshAndContour(self, imgHSV, np.array([100, 112, 197]), np.array([114, 160, 230]))
            height, width = result.shape[:2]
            blank = np.zeros((height, width), np.uint8)

            for c in contours:
                x, y, w, h = cv2.boundingRect(c)
                ratio = w/h
                if 0.8 < ratio/targetRatio < 1.2:
                    locatedTargets.append(c)
            #for t in locatedTargets:
            blank = cv2.drawContours(blank, locatedTargets, -1, 255, 3)
            return blank

        elif function == 'bothAC':
            result, both, contours = self.bothAndContours(self, imgHSV, np.array([100, 112, 197]), np.array([114, 160, 230]), 'median')
            height, width = result.shape[:2]
            blank = np.zeros((height, width), np.uint8)

            print('cnts', len(contours))

            for c in contours:
                x, y, w, h = cv2.boundingRect(contours[0])
                print('w-', w, 'h-', h)
                ratio = w / h
                if 0.2 < ratio/targetRatio < 1.8:
                    print(ratio/targetRatio)
                    locatedTargets.append(c)

            print("locatd", len(locatedTargets))
            blank = cv2.drawContours(blank, locatedTargets, -1, (0, 255, 0), 3)
            return result

        else:
            result, contours = self.contours(imgHSV)
            height, width = result.shape[:2]
            blank = np.zeros((height, width), np.uint8)
            
            for c in contours:
                x, y, w, h = cv2.boundingRect()
                ratio = w/h
                if 0.2 < ratio/targetRatio < 1.8:
                    locatedTargets.append(c)
            for t in locatedTargets:
                blank = cv2.drawContours(blank, t, -1, (0, 255, 0), 3)
            return blank

            
