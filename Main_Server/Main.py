import numpy
from Main_Server import Calibrate
from Main_Server import Communication
#from GlobalData import HSV_highThresh
#from GlobalData import HSV_lowThresh
#from GlobalData import currentFrame
#from GlobalData import hsvImg
import threading


com = Communication.Comm()
com.daemon = True
com.run()



def debugMode():
    cal = Calibrate.Calib(5991)
    cal.daemon = True
    cal.start()

