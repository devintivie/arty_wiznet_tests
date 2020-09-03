
INTERVAL = "apg:int"
PATTERN = "apg:patt"
PINGPONG = "apg:ping"
STATUS = "apg:stat"
TIMING = "apg:tim"
TEST = "apg:test"
MASK_GLOBALA = "apg:mask:glob:a"
MASK_GLOBALB = "apg:mask:glob:b"
MASK_BLOCKA0 = "apg:mask:block:a0"
MASK_BLOCKA = "apg:mask:block:a"
MASK_BLOCKB0 = "apg:mask:block:b0"
MASK_BLOCKB = "apg:mask:block:b"
MASK_INTERLOCK = "apg:mask:int"
MASK_REMOTE = "apg:mask:rem"
MASK_PORTA = "apg:mask:port:a"
MASK_PORTB = "apg:mask:port:b"
MASK_PORTC = "apg:mask:port:c"
MASK_PORTD = "apg:mask:port:d"
MASK_INVERTA = "apg:mask:inv:a"
MASK_INVERTB = "apg:mask:inv:b"
MASK_INVERTC = "apg:mask:inv:c"
MASK_INVERTD = "apg:mask:inv:d"
TRIGGER_SELECT = "apg:trig:sel"
TRIGGER_DELAY = "apg:trig:del"
ADD_PULSE = "apg:puls:add"

import on_off_classes as on_off

class pattern_generator:
    def __init__(self, client):
        self.client = client

    def set_interval_length(self, length):
        tempString = f"{INTERVAL} {length}"
        return self.client.send(tempString)

    def get_interval_length(self):
        tempString = f"{INTERVAL}?"
        return self.client.send(tempString)

    def set_pattern_length(self, length):
        tempString = f"{PATTERN} {length}"
        return self.client.send(tempString)

    def get_pattern_length(self):
        tempString = f"{PATTERN}?"
        return self.client.send(tempString)

    def set_pingpong_length(self, length):
        tempString = f"{PINGPONG} {length}"
        return self.client.send(tempString)

    def get_pingpong_length(self):
        tempString = f"{PINGPONG}?"
        return self.client.send(tempString)

    def set_timing(self, setting):
        setString = on_off.on_off_to_string(setting)
        tempString = f"{TIMING} {setString}"
        return self.client.send(tempString)
        
    def get_timing(self):
        tempString = f"{TIMING}?"
        return self.client.send(tempString)
        

    # def set_mask(APGMasks mask, int value):
    #     tempString = f"{MaskDict[mask]] {value}"
    #     return self.client.send(tempString)
        

    # def get_mask(APGMasks mask, bool hex):
    #     tempString = f"{MaskDict[mask]}?"
    #     resp = self.client.send(tempString)

    #     return resp.ToValueString(hex)
        

    def check_status(self):
        tempString = f"{STATUS}?"
        return self.client.send(tempString)
        
        
    def set_to_test(self):
        tempString = f"{TEST}"
        return self.client.send(tempString)
        

    def add_pulse(self, startIndex, stopIndex, value):
        tempString = f"{ADD_PULSE} {startIndex} {stopIndex} {value}"
        return self.client.send(tempString)
        

