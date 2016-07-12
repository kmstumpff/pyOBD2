import Interface
import socket

class IPInterface(Interface.Interface):
    def __init__(self):
        self.type = Interface.IP
        self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def setHost(self, host):
        self.host = host

    def setPort(self, port):
        self.port = port

    def connect(self, timeout_l):
        self.timeout = timeout_l
        self.conn.connect((self.host, self.port))
        self.conn.settimeout(self.timeout)

    def initialize(self):
        DELAY = 1
        self.write("AT D \r")
        time.sleep(DELAY)
        print self.read(64)
        self.write("AT Z \r")
        time.sleep(DELAY)
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

    def write(self, command):
        self.conn.send(command)

    def read(self, length):
        #print "Bytes available: " + str(self.conn.in_waiting)
        #print "Bytes reading: " + str(len)
        return self.conn.recv(length)
