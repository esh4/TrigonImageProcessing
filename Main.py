import cv2
from server import ComProtocol
#from FilterHSV import FiltHSVs

serv = ComProtocol(5990)
serv.conn()

cam = cv2.VideoCapture(0)       #create camera object
tf, frame = cam.read()          #read pic from cam
cv2.imwrite('output.jpg', frame)

serv.sendImageFile(open('output.jpg', 'rb'))







cam.release()