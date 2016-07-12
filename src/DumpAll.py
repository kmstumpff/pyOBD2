import OBD2
import Interface

def example():
    #car = OBD2.OBD2(Interface.SERIAL, path="/dev/pts/10")
    car = OBD2.OBD2(Interface.IP, host="192.168.0.10", port=35000)

    car.connect(timeout=0.2)

    for pid in range(0x00, 0xFF):
        print hex(pid) + " = " + car.readPID(0x01, pid, 0x1C)
        #time.sleep(0.9)


if __name__ == "__main__":
    example()
