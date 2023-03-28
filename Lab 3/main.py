import serial, struct
from file import Sensor

class SerialPort:
    def __init__(self,port,baudrate):
        self.serial_port = serial.Serial()
        self.port = port
        self.baudrate = baudrate

    def open(self):
        if not self.serial_port.is_open:
            self.serial_port.port = self.port
            self.serial_port.baudrate = self.baudrate
            self.serial_port.open()

    def is_open(self):
        return self.serial_port.is_open
       
    def read_data(self):
        return self.serial_port.readline().decode().strip()

    def write_data(self,data):
        self.serial_port.write(struct.pack(">B",data))


def process(max,min):
    port.open()
    if port.is_open():
        while(True):
            data = int(port.read_data())

            if data < min:
                data = min
            if data > max:
                data = max
            else:
                data = data

            data = int((max - data) * 255 / (max - min))
            print("Dato enviado ",data)      
            port.write_data(data)


def menu():
    x = 0
    while x == 0:
        print("\nMENU.")
        print("\n1. Set up values for sensor.")
        print("2. Read data.")
        resp = int(input("Enter an option (1 or 2): "))

        if resp == 1:
            values = []
            max = int(input("Enter the maximum value for the sensor: "))
            min = int(input("Enter the minimum value for the sensor: "))
            values.append(max)
            values.append(min)
            Sensor.register(values)

        elif resp == 2:
            if len(values) == 0:
                print("\nThere are no registered values.")
            else:
                maxmin = []
                maxmin = Sensor.lecture()
                process(int(maxmin[0]),int(maxmin[1]))

port = SerialPort("COM3",9600)
menu()


