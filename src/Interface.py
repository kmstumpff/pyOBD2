SERIAL = 0
IP = 1

class Interface:
    def __init__(self):
        raise NotImplementedError()

    def getType(self):
        return self.type

    def setPath():
        raise NotImplementedError()

    def setHost():
        raise NotImplementedError()

    def setPort():
        raise NotImplementedError()

    def connect():
        raise NotImplementedError()

    def write(self, msg):
        raise NotImplementedError()

    def read(self, msg, len, timeout=0):
        raise NotImplementedError()
