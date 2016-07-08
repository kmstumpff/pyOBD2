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


    def readPID(self, mode, pid, numBytes):
        #print "write(" + pid + ")"
        self.interface.write(getPIDString(mode, pid) + self.NL)
        temp = self.interface.read(8)
        #print "read(" + temp + ")"
        response = self.interface.read(5 + (numBytes * 3)) # two characters and a space per byte
        #print "read(" + response + ")"
        temp = self.interface.read(3)
        #print "read(" + temp + ")"
        #print response
        ret = response[6:] # ignore the first 6 characters (mode, pid)

        return ret

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
