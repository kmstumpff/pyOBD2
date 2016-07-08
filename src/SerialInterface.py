import Interface
import serial

class SerialInterface(Interface.Interface):
    def __init__(self):
        self.type = Interface.SERIAL

    def setPath(self, path):
        self.path = path

    def connect(self, timeout_l):
        self.conn = serial.Serial(self.path, baudrate=38400, timeout=timeout_l)

    def write(self, command):
        self.conn.write(command)

    def read(self, len):
        #print "Bytes available: " + str(self.conn.in_waiting)
        #print "Bytes reading: " + str(len)
        return self.conn.read(len)
