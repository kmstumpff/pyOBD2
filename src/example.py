import OBD2
import Interface

def example():
    car = OBD2.OBD2(Interface.SERIAL, path="/dev/pts/10")
    #car = OBD2(IP, host="192.168.0.10", port=35000)

    car.connect()



if __name__ == "__main__":
    example()
