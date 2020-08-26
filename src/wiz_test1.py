from wiz_scpi import *

wiz = wiz_scpi('169.254.208.100')
try:
    wiz.connect()
    print(wiz.Firmware)
    print(wiz.Identity)
    # wiz.change_ip('169.254.208.100')

    print(wiz.set_register(15, 10))
    print(wiz.get_register(15))
    print(wiz.reset())
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