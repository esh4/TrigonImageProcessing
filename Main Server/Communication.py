from GlobalData import posData
from networktables import NetworkTable
import logging
import threading

class Comm(threading.Thread):
    def __init__(self):
        threading.Thread.__init__()

    def run(self):
        logging.basicConfig(level=logging.DEBUG)
        global posData

        NetworkTable.setIPAddress("XX.XX.XX.XX")  # Change the address to client IP
        NetworkTable.setClientMode()
        NetworkTable.initialize()
        sd = NetworkTable.getTable("SmartDashboard")

        sd.putNumber('DistanceToReflector', posData[0])
        sd.putNumber('AngleToReflector', posData[1])

