import socket
import cv2
from networktables import networktable
import logging

logging.basicConfig(level=logging.DEBUG)

HSVvalues = []

class Debug:
    def __init__(self, port):
        self.port = port

    def connect(self):
        print "-> Ready"
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('0.0.0.0', self.port))
        s.listen(1)
        print 'wait for connect'
        conn, address = s.accept()
        self.conn = conn
        print address

    def sendImage(self, img):
        a = ''
        for n in img:
            if len(a) == 100 or len(a) > 100:
                self.conn.send(a)
                a = ''
                a += n
            else:
                a += n
        self.conn.send(a)
        print 'done'
        self.conn.send("done")
        img.close()

class ProcessImage:
    def __init__(self):
        pass

    def filterImg(self, img):
        HSVimg = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        filtHSVimg = cv2.inRange(HSVimg,HSVvalues)
        return filtHSVimg

    def contourReport(self, img):
        contours = cv2.findContours(img)
        for i in contours:
            pass #find all the info for each contour,
        #find correct contour.
        #return contour info.
        pass

class Comms:
    def __init__(self):
        pass


