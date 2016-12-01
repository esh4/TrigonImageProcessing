import cv2
from server import ComProtocol, FilterImage



'''
serv = ComProtocol(5990)
serv.conn()

cam = cv2.VideoCapture(0)       #create camera object
tf, frame = cam.read()          #read pic from cam
cam.release()
FiltIMG = FilterImage()

imgHSV = FiltIMG.filterBar(frame)

cv2.imwrite('output.jpg', imgHSV)
#cv2.imwrite('output.jpg', frame)

serv.sendImageFile(open('output.jpg', 'rb'))

'''

