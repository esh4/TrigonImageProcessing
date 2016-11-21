import socket
import numpy as np
import cv2

class ComProtocol:
    def __init__(self, port):
        self.port = port

    def conn(self):
        print "-> Ready"
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('0.0.0.0', self.port))
        s.listen(1)
        print 'wait for connect'
        conn, address = s.accept()
        self.conn = conn
        print address

    #def SendVideoFeed(self):

    def sendImageFile(self, img):
        a = ''
        for n in img:
            if len(a) == 100 or len(a)>100:
                self.conn.send(a)
                a = ''
                a += n
            else:
                a += n
        print 'done'
        self.conn.send('done')
        img.close()