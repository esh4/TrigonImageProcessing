<<<<<<< HEAD
import socket
import cv2
from PIL import Image

msg = raw_input("->")

s = socket.socket()
s.connect(('10.59.90.43', 5990))
#10.59.90.43
print "Connected!"

img = open("input.jpg", 'wb')
#s.send(msg)
while True:
    data = s.recv(100)
    if data == "done":
        #img.write(data)
        break
    else:
        img.write(data)

img.close()


s.close()
=======
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



s.close()
>>>>>>> master
