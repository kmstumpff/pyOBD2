import Interface

class IPInterface(Interface.Interface):
    def __init__(self):
        self.type = Interface.IP

    def setHost(self, host):
        self.host = host

    def setPort(self, port):
        self.port = port
