import time
import OBD2
import Interface

def example():
    car = OBD2.OBD2(Interface.SERIAL, path="/dev/pts/5")
    #car = OBD2(IP, host="192.168.0.10", port=35000)

    car.connect()

    while(True):
        rpm = car.getRPMs()
        speed = car.getSpeed()
        print "RPM: " + str(rpm) + " Speed: " + str(speed)
        #time.sleep(0.9)


if __name__ == "__main__":
    example()
