import Interface

class IPInterface(Interface.Interface):
    def __init__(self):
        self.type = Interface.IP
        self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def setHost(self, host):
        self.host = host

    def setPort(self, port):
        self.port = port

    def connect(self, timeout_l):
        self.conn.connect((self.host, self.port))

    def write(self, command):
        self.conn.send(command)

    def read(self, len):
        #print "Bytes available: " + str(self.conn.in_waiting)
        #print "Bytes reading: " + str(len)
        return self.conn.receive(len)
