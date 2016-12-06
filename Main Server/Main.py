import cv2
from Classes import ProcessImage
import threading
import socket

HSVvalues = []
frameData = []
ImageProcess = ProcessImage()

IP = threading.Thread(target=ImageProcess.mainProcess(), args=(0, ))
IP.setDaemon(True)
IP.start()