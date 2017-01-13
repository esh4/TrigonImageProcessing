import numpy
import Calibrate
import Communication
from GlobalData import HSV_highThresh
from GlobalData import HSV_lowThresh
from GlobalData import currentFrame
from GlobalData import hsvImg
import threading
import thread

def normalNormal():
    com = Communication.Comm()
    com.daemon = True
    com.start()



def debugMode():
    cal = Calibrate.Calib(5991)
    cal.daemon = True
    cal.start()