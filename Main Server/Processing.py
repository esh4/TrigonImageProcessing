from GlobalData import HSV_highThresh
from GlobalData import HSV_lowThresh
from GlobalData import currentFrame
from GlobalData import hsvImg
from GlobalData import posData
import cv2
import threading


class ImageProcess(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global currentFrame
        global hsvImg
        global posData

        currentFrame = self.capImg(0)
        hsvImg, posData = self.filterImg(currentFrame)

    def capImg(self, camIndex):
        cam = cv2.VideoCapture(camIndex)
        tr, frame = cam.read()
        cam.release()
        return frame

    def filterImg(self, img):
        global HSV_lowThresh
        global HSV_highThresh
        HSVimg = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        filtHSVimg = cv2.inRange(HSVimg, HSV_lowThresh, HSV_highThresh)
        data = []
        return filtHSVimg, data