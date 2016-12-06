import numpy
import Calibrate
from GlobalData import HSV_highThresh
from GlobalData import HSV_lowThresh
from GlobalData import currentFrame
from GlobalData import hsvImg

calib = Calibrate.Calib(5991)

try:
    calib.run()

except Exception, e:
    print e.message

raw_input()



