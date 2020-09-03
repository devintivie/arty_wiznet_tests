from socket_control import socket_control
from pattern_generator import *
from sensor_control import *

IDENTIFY = "*idn?"
RESET = "*rst"
REGISTER = "syst:reg"
FIRMWARE = "syst:firm"
SET_IP = "syst:ip"

class wiz_scpi(socket_control):
    def __init__(self, iAddr, iPort = 5025):
        super().__init__(iAddr, iPort)
        self.Firmware = None
        self.Identity = None

        self.apg = pattern_generator(self)
        self.sensor = sensor_control(self)

    def connect(self):
        super().connect()
        if self.Socket:
            self.get_firmware()
            self.get_identity()

    def get_firmware(self):
        self.Firmware = self.send(f"{FIRMWARE}?")

    def get_identity(self):
        self.Identity = self.send(f"{IDENTIFY}")

    def reset(self):
        return self.send(f"{RESET}")

    def change_ip(self, newIP):
        self.send(f"{SET_IP} {newIP}")

    def set_register(self, register, value):
        tempString = f"{REGISTER} {register} {value}"
        return self.send(tempString)

    def get_register(self, register):
        tempString = f"{REGISTER}? {register}" 
        return self.send(tempString)

    


