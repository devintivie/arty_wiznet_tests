REGISTER = "syst:reg"
def set_register(self, register, value):
    tempString = f"{REGISTER} {int(register)} {int(value)}"
    return self.Send(tempString)