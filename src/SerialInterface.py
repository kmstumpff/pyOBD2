import Interface
import serial

class SerialInterface(Interface.Interface):
    def __init__(self):
        self.type = Interface.SERIAL

    def setPath(self, path):
        self.path = path

    def connect(self):
        self.conn = serial.Serial(self.path, baudrate=38400, timeout=1)

    def write(self, command):
        self.conn.write(command)

    def read(self, len, timeout):
        # TODO -- len, timeout
        return self.conn.read(len)
