#!/bin/python

import socket
import time

IP = "192.168.0.10"
PORT = 35000
BUFFER_SIZE = 1024
SLEEP = 0.25
SLEEP_INC = 0.05

car = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

car.connect((IP, PORT))

def stringToHex(theStr):
    hexStr = ""
    for x in theStr:
        hexStr = hexStr + "0x" + x.encode('hex') + " "
    return hexStr
def bytesToInt(a, b):
    return (((a*256)+b)/4)

"""
# Reset
car.send('atz' + bytearray('\x0D'))
time.sleep(10)
resp = car.recv(BUFFER_SIZE)
print resp

# Read voltage
car.send('atrv' + bytearray('\x0D'))
resp = car.recv(BUFFER_SIZE)
print stringToHex(resp)

# Get PIDs
car.send(bytearray('\x01\x00\x0D'))
resp = car.recv(BUFFER_SIZE)
print stringToHex(resp)
"""
try:

    # Set the protocol to ISO 9141
    req = 'AT SP 3 \r\r'
    car.send(req)
    time.sleep(1)
    resp = car.recv(BUFFER_SIZE)




    while(True):
        try:
            req = '01 0C \r\r'
            car.send(req)
            time.sleep(SLEEP)
            resp = car.recv(BUFFER_SIZE)
            byteA = int((resp[13] + resp[14]), 16)
            byteB = int((resp[16] + resp[17]), 16)
            print str(bytesToInt(byteA, byteB)) + " RPM"
        except IndexError as e:
            SLEEP = SLEEP + SLEEP_INC
            if SLEEP > 1:
                print "Giving up..."
                quit()
            else:
                print "time too quick. increasing to " + str(SLEEP)
        except ValueError as e:
            SLEEP = SLEEP + SLEEP_INC
            if SLEEP > 1:
                print "Giving up..."
                quit()
            else:
                print "time too quick. increasing to " + str(SLEEP)
except KeyboardInterrupt as e:
    print "Closing connection"
car.close()
