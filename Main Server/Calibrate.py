import socket
import cv2

class Calib:
    def __init__(self, PCport):
        self.port = PCport

    def run(self):

        global HSV_lowThresh
        global HSV_highThresh
        global currentFrame
        global hsvImg

        self.connect()
        func = self.getCommands()

        if func[0] == -1: pass
        else: HSV_lowThresh = func[0]

        if func[1] == -1: pass
        else: HSV_highThresh = func[1]

        if func[2] == False: pass
        else: self.sendImage(currentFrame)

        if func[3] == False: pass
        else: self.sendImage(hsvImg)

    def connect(self):
        print "-> Ready"
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('0.0.0.0', self.port))
        s.listen(1)
        print 'wait for connect'
        conn, address = s.accept()
        self.conn = conn
        print address

'''
PC commands:
    [(lowThresh), (highThresh), getImage(bool), getHSVimg(bool)]
'''

    def getCommands(self, command=-1):
        PCin = []
        PCin.append(self.conn.recv(1024))
        return PCin

    def saveImg(self, img):
        cv2.imwrite('sendPic.jpg', img)
        return None

    def sendImage(self, CVimg):
        self.saveImg(CVimg)
        img = open('sendPic.jpg', 'rb')
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
        #self.conn.send("done")
        img.close()