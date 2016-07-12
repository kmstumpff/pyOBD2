SERIAL = 0
IP = 1

class Interface:
    def __init__(self):
        raise NotImplementedError()

    def getType(self):
        return self.type

    def setPath(self, path):
        raise NotImplementedError()

    def setHost(self, host):
        raise NotImplementedError()

    def setPort(self, port):
        raise NotImplementedError()

    def connect(self, timeout_l):
        raise NotImplementedError()

    def initialize(self):
        raise NotImplementedError()

    def write(self, msg):
        raise NotImplementedError()

    def read(self, length):
        raise NotImplementedError()
