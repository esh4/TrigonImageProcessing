import socket
import cv2
from PIL import Image

msg = raw_input("->")

s = socket.socket()
s.connect(('127.0.0.1', 5990))

print "Connected!"

img = open("input.jpg", 'wb')
s.send(msg)
while True:
    data = s.recv(100)
    if data == "done":
        img.write(data)
        break
    img.write(data)

img.close()

im = Image.open("input.jpg")
im.show()

s.close()
