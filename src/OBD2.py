# Interfaces
import Interface
import IPInterface
import SerialInterface
import PID
import math
import time

def getPIDString(mode, pid):
    return "".join("{:02X}".format(mode)) + " " + "".join("{:02X}".format(pid))

class OBD2:
    def __init__(self, type, path="", host="", port=0):
        self.NL = '\n'
        if(type == Interface.SERIAL):
            self.interface = SerialInterface.SerialInterface()
            self.interface.setPath(path)
        elif(type == Interface.IP):
            self.interface = IPInterface.IPInterface()
            self.interface.setHost(host)
            self.interface.setPort(port)
        else:
            raise Exception("Invalid Interface Type")

    def connect(self, timeout=2):
        self.interface.connect(timeout)

    def initialize(self):
        self.interface.initialize()


    def readPID(self, mode, pid, numBytes):
        #print "write(" + pid + ")"
        self.interface.write(getPIDString(mode, pid) + self.NL)
        response = self.interface.read(7 + (numBytes * 2)) # two characters and a space per byte
        return response[5:(5+(numBytes*2))] # ignore the first 5 characters ('\r', mode, pid)

    def getRPMs(self):
        res = self.readPID(1, PID.RPM, 2)
        arr = res.split(' ')
        a = int(arr[0], 16)
        b = int(arr[1], 16)
        return (((256*a) + b) / 4)

    def getSpeed(self):
        res = self.readPID(1, PID.SPEED, 1)
        a = int(res, 16)
        return math.floor(a * 1.60934400061)
