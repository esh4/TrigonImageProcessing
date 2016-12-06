import cv2
import socket


class ProcessImage:
    def __init__(self):
        global HSVvaules
        self.hsv = HSVvaules

    def capImg(self, camIdex):
        cam = cv2.VideoCapture(camIdex)
        tr, frame = cam.read()
        cam.release()
        return frame

    def filterImg(self, img):
        HSVimg = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        filtHSVimg = cv2.inRange(HSVimg, self.hsv)
        return filtHSVimg

    def contourReport(self, img):
        contours = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        maxSize = 0
        for i in contours:
            if cv2.contourArea(contours[i]) > maxSize:
                correctCont = contours[i]
                #find all the info for each contour,
        #find correct contour.
        #return contour info.
        return correctCont

    def mainProcess(self, camIndex=0):
        global frameData
        while True:
            frame = self.capImg(camIndex)
            frameData = self.contourReport(self.filterImg(frame))






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

    def getCommands(self):
        return self.conn.recv(1024)

    def sendImage(self, img):
        a = ''
        if self.conn.recv(100) == "pic":
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