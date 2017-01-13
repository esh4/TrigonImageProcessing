from GlobalData import posData
from networktables import NetworkTable
import logging
import threading
import time
    
class Comm(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        NetworkTable.setClientMode()
        NetworkTable.setIPAddress("10.59.90.221")  # Change the address to client IP
        NetworkTable.initialize()
        logging.basicConfig(level=logging.DEBUG)

        self.sd = NetworkTable.getTable('SmartDashboard')


    def run(self):
        while True:
            print "befire"
            self.sd.putNumber('DistanceToReflector', 2)
            self.sd.putNumber('AngleToReflector', 3)
            print "after"
            time.sleep(1)

