import Interface
import serial
import time

class SerialInterface(Interface.Interface):
    def __init__(self):
        self.type = Interface.SERIAL

    def setPath(self, path):
        self.path = path

    def connect(self, timeout_l):
        self.timeout = timeout_l
        self.conn = serial.Serial(self.path, baudrate=38400, timeout=self.timeout)

    def initialize(self):
        DELAY = 1
        self.conn.timeout = 0
        self.write("AT D \r")
        time.sleep(DELAY)
        print self.read(64)
        self.write("AT Z \r")
        time.sleep(DELAY*2)
        print self.read(64)
        self.write("AT E0 \r")
        time.sleep(DELAY)
        print self.read(64)
        self.write("AT L0 \r")
        time.sleep(DELAY)
        print self.read(64)
        self.write("AT S0 \r")
        time.sleep(DELAY)
        print self.read(64)
        self.write("AT H0 \r")
        time.sleep(DELAY)
        print self.read(64)
        self.write("AT SP 0 \r")
        time.sleep(DELAY)
        print self.read(64)
        self.conn.timeout = self.timeout

    def write(self, command):
        self.conn.write(command)

    def read(self, length):
        #print "Bytes available: " + str(self.conn.in_waiting)
        #print "Bytes reading: " + str(len)
        return self.conn.read(length)
