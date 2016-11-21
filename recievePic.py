import socket
import cv2

msg = raw_input("->")

s = socket.socket()
s.connect(('192.168.1.100', 5990))

print "Connected!"

img = open("input.jpg", 'wb')
s.send(msg)
while True:
    data = s.recv(100)
    if data == "done":
        break
    img.write(data)

img.close()

img = open("input.jpg", 'r')
cv2.namedWindow("picture")
cv2.imshow("picture", img)


s.close()
