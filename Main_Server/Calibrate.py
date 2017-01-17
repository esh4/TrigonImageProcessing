import socket
import cv2
import Processing
from GlobalData import HSV_highThresh
from GlobalData import HSV_lowThresh
from GlobalData import currentFrame
from GlobalData import hsvImg

class Calib():
    def __init__(self, port):
        self.port = port

    def run(self):

        global HSV_lowThresh
        global HSV_highThresh
        global currentFrame
        global hsvImg

        self.connect()

        while True:
            func = self.getCommands()

            '''
            getCommands returns the following list:
                [(LH, LS, LV), (UH, US, UV), getImage, getHSVimg]
            '''
            print( "func ", func)

            if func[0] == (-1, -1, -1): pass
            else: HSV_lowThresh = func[0]

            if func[1] == (-1, -1, -1): pass
            else: HSV_highThresh = func[1]

            if func[2] == False: pass
            else: self.sendImage(currentFrame)

            if func[3] == False: pass
            else:
                hsvImg = Processing.Processing.filterRectBasic(Processing.Processing.toHSV(cv2.imread('sendPic.jpg', -1)), 5, 4, 'bothAC')
                self.sendImage(hsvImg)

    def connect(self):
        print( "-> Ready")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('0.0.0.0', self.port))
        s.listen(1)
        print( 'wait for connect')
        conn, address = s.accept()
        print(address)
        self.conn = conn
        return None

    '''
    PC commands:
        [LH, LS, LV, UH, US, UV, getImage(bool), getHSVimg(bool)]
    '''

    def getCommands(self, command=-1):
        PCin = self.conn.recv(1024)
        PCin = PCin .decode("utf-8").split(',')
        print( "input from client: ", PCin)
        lThresh = []
        hThresh = []
        out = []

        for i in range(3):
            lThresh.append(PCin[i])

        for i in range(3, 6):
            hThresh.append(PCin[i])

        lThresh = tuple(lThresh)
        hThresh = tuple(hThresh)

        print(lThresh)
        print(hThresh)

        out.append(lThresh)
        out.append(hThresh)

        for i in range(6, 8):
            out.append(self.checkBool(PCin[i]))

        return out

    def checkBool(self, i):
        if i == 't': return True
        elif i == 'f': return False
        else: return "blank"

    def saveImg(self, img):                     #don't run method, it is called from sendImage method.s
        #cv2.imwrite('sendPic.jpg', img)
        return None

    def sendImage(self, CVimg):
        self.saveImg(CVimg)
        img = open('sendPic.jpg', 'rb')
        a = b''
        counter = 0
        for n in img:
            if len(a) == 100 or len(a) > 100:
                self.conn.send(a)
                a = b''
                a += n
            else:
                a += n

        self.conn.send(a)
        print( 'done')
        self.conn.send(b"done")
        img.close()
