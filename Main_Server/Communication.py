#from GlobalData import posData
from networktables import NetworkTables
import logging
import threading
import time


class Comm():
    def __init__(self):
        logging.basicConfig(level=logging.DEBUG)
        NetworkTables.setClientMode()
        NetworkTables.setIPAddress("10.59.90.2")  # Change the address to client IP
        NetworkTables.initialize()

        self.sd = NetworkTables.getTable('SmartDashboard')

    def run(self):
        while True:
            print("before")
            self.sd.putNumber('DistanceToReflector', 2)
            self.sd.putNumber('AngleToReflector', 3)
            print("after")
            time.sleep(1)
