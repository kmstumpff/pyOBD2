# Interfaces
import Interface
import IPInterface
import SerialInterface

class OBD2:
    def __init__(self, type, path="", host="", port=0):
        if(type == Interface.SERIAL):
            self.interface = SerialInterface.SerialInterface()
            self.interface.setPath(path)
        elif(type == Interface.IP):
            self.interface = IPInterface.IPInterface()
            self.interface.setHost(host)
            self.interface.setPort(port)
        else:
            raise Exception("Invalid Interface Type")

    def connect(self):
        self.interface.connect()

    def write(self, msg):
        self.interface.write(msg)

    def read(self, len, timeout=0):
        return self.interface.read(len, timeout)
