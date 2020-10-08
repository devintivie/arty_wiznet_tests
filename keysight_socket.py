from socket_control import socket_control
from time import sleep

class keysight_socket(socket_control):
    def __init__(self, iAddr, iPort = 5025):
        super().__init__(iAddr, iPort)

    def send(self, command):
        if not command.endswith('\n'):	
            command = command + '\n'
        return super().send(command)

    def set_trigger_holdoff(self, hold):
        try:
            holdoff = float(hold)
        finally:
            pass
        tempValue = '{:.2e}'.format(holdoff)
        tempString = f"TRIG:HOLD {tempValue}"
        return self.send(tempString)

    

if __name__ == "__main__":
    test = socket_control('169.254.9.155', 5025)
    print(test.is_connected)

    try:
        test.connect()
        sleep(0.5)
        print(test.is_connected)
        resp = test.send(':TRIG:HOLD?\n')
        print(f"resp = {resp}")
        sleep(1)

    finally:
        test.close()
        print(test.is_connected)
