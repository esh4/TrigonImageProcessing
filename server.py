import socket
import numpy as np
import cv2
'''def main():
    capWebcam = cv2.VideoCapture(0)
    
    if not capWebcam.isOpened():
        print "Webcam not accessed successfully \n\n"
        os.system("pause")
        return
    out = cv2.VideoWriter('output.avi', -1, 20.0, (640,480))
    while cv2.waitKey(1)!= 27 and capWebcam.isOpened():
        frameRead, frame = capWebcam.read()
        
        if not frameRead or frame is None:
            print "no image avialable\n"
            os.system("pause")
            break
        
        cv2.namedWindow("VideoFeed", cv2.WINDOW_NORMAL)
        
        cv2.imshow("VideoFeed", frame)
        out.write(frame)
        



if __name__ == "__main__":
    main()'''
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

    #def SendVideo(self):

    def sendImageFile(self, img):
        a = ''
        for n in img:
            if len(a) == 100 or len(a)>100:
                self.conn.send(a)
                a = ''
            else:
                a+=n
        print 'done'
        self.conn.send('done')