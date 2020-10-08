from wiz_scpi import *

from time import sleep

wiz = wiz_scpi('169.254.208.100')
try:
    wiz.connect()
    print(wiz.Firmware)
    print(wiz.Identity)
    # wiz.change_ip('169.254.208.100')

    print(wiz.set_register(15, 10))
    print(wiz.get_register(15))

    # print(wiz.apg.set_pattern_length(1500))
    # print(wiz.apg.get_pattern_length())
    # print(wiz.apg.set_pattern_length(500))
    # print(wiz.apg.get_pattern_length())
    # print(wiz.apg.set_pingpong_length(50))
    # print(wiz.apg.get_pingpong_length())
    # print(wiz.apg.set_timing('True'))
    # print(wiz.apg.get_timing())
    print(wiz.sensor.set_sensor_power('ch1', True))
    print(wiz.sensor.get_sensor_power('ch1'))
    print(wiz.get_register(0))
    print(wiz.get_register(4))

    sleep(1)

    print(wiz.sensor.set_sensor_power('ch1', 'Off'))
    print(wiz.sensor.get_sensor_power('ch1'))
    print(wiz.get_register(0))
    print(wiz.get_register(4))

    sleep(0.5)
    # print(wiz.sensor.set_sensor_power('ch1', True))
    print(wiz.sensor.get_sensor_power('ch1'))
    print(wiz.get_register(0))
    print(wiz.get_register(4))

finally:
    wiz.close()
# from wiz_scpi import *

# import WiznetRegisterCommands


# wiz = wiz_scpi('169.254.208.100')
# try:
#     wiz.Connect()
#     print(wiz.Firmware)
#     print(wiz.Identity)

#     print(WiznetRegisterCommands.SetRegister(wiz, 10,15))

# finally:
#     wiz.Close()