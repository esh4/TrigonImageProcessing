import numpy
import Calibrate
from GlobalData import HSV_highThresh
from GlobalData import HSV_lowThresh
from GlobalData import currentFrame
from GlobalData import hsvImg



'''
    3 Parts:
        -Calibrate( ):
            communicates with PC. updates HSV, request Image for PC.
        
        -processing( ):
            takes pictures
            gets useful info

        -Robot Comms( ):
            sends the robot the useful info.
'''

calib = Calibrate.Calib(5991)

try:
    calib.run()

except Exception, e:
    print e.message

raw_input()



