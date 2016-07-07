import time
import OBD2
import Interface

def example():
    car = OBD2.OBD2(Interface.SERIAL, path="/dev/pts/10")
    #car = OBD2(IP, host="192.168.0.10", port=35000)

    car.connect()

    while(True):
        car.write("01 0C\n")
        car.read(8) # Throw away echo characters
        print car.read(12)
        car.read(2) # Throw away prompt characters
        time.sleep(1)


if __name__ == "__main__":
    example()
