import cv2
from server import ComProtocol

serv = ComProtocol(5990)
serv.conn()

cam = cv2.VideoCapture(0)


tf, frame = cam.read()
cv2.imwrite('output.jpg', frame)
#picBin = frame.astype('String')  #srting of bytes

serv.sendImageFile(open('output.jpg', 'rb'))

cam.release()