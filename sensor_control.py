POWER = "sens:pow"
STATUS = "sens:status"
TRIGGER_DELAY = "sens:trig:del"
TRIGGER_SELECT = "sens:trig:sel"
TRIGGER_ARM = "sens:trig:arm"
TRIGGER_STATE = "sens:trig:stat"
TRIGGER_PRESENT = "sens:trig:pres"
TIMESTAMP = "sens:timestamp"

import on_off_classes as on_off

from enum import Enum

class sensor_control:
    def __init__(self, client):
        self.client = client

    def set_sensor_power(self, sensor, setting, toLog = True):
        chValue = to_channel(sensor)
        setString = to_onoff_string(setting)

        tempString = f"{POWER} {chValue} {setString}"
        print(tempString)
        return self.client.send(tempString)
        
    def get_sensor_power(self, sensor):
        chValue = to_channel(sensor)

        tempString = f"{POWER}? {chValue}"
        return self.client.send(tempString)

    def set_trigger_delay(self, sensor, pulses, toLog = True):
        chValue = to_channel(sensor)

        tempString = f"{TRIGGER_DELAY} {chValue} {pulses}"
        return self.client.send(tempString, toLog)

    def get_trigger_delay(self, sensor, toLog = True):
        chValue = to_channel(sensor)

        tempString = f"{TRIGGER_DELAY}? {chValue}"
        return self.client.send(tempString, toLog)
        
    def set_trigger_select(self, sensor, opt, toLog = True):
        chValue = to_channel(sensor)
        optInt = opt#(int)opt
        tempString = f"{TRIGGER_SELECT} {chValue} {optInt}"
        return self.client.send(tempString, toLog)

    def get_trigger_select(self, sensor, toLog = True):
        chValue = to_channel(sensor)
        tempString = f"{TRIGGER_SELECT}? {chValue}"
        return self.client.send(tempString, toLog)

    def get_trigger_state(self, sensor, toLog = True):
        chValue = to_channel(sensor)
        tempString = f"{TRIGGER_STATE}? {chValue}"
        resp =  self.client.send(tempString, toLog)

        try:
            state = TriggerState(int(resp))
            return state
        finally:
            print(resp)
    
    def get_triggers_present(self, toLog = True):
        tempString = f"{TRIGGER_PRESENT}?"
        resp = self.client.send(tempString, toLog)
        fm = False
        ztc = False
        pol = False
        irig = False

        try:
            data = int(resp)
        finally:
            pass




        # public async Task<TriggersPresent> GetTriggerPresent(toLog = True):
        #     var tempString = f"{WiznetSensorCommands.TRIGGER_PRESENT}?"
        #     var resp = await Send(tempString, toLog)
        #     var fm = false
        #     var ztc = false
        #     var pol = false
        #     var irig = false
        #     if(int.TryParse(resp, out var data))
        #     {
        #         if ((data & 0x1) == 1)
        #         {
        #             fm = true
        #         }
        #         if(((data >> 1) & 0x1) == 1)
        #         {
        #             ztc = true
        #         }
        #         if (((data >> 2) & 0x1) == 1)
        #         {
        #             pol = true
        #         }
        #         if (((data >> 3) & 0x1) == 1)
        #         {
        #             irig = true
        #         }
        #     }

        #     return new TriggersPresent(fm, ztc, pol, irig)
        # }

        
        # public async Task<SensorStatus> GetSensorStatus(int sensor, toLog = True):
        #     var chValue = f"ch{sensor}"
        #     var tempString = f"{WiznetSensorCommands.Status}? {chValue}"
        #     var resp = await Send(tempString, toLog)
        #     var power = false
        #     var oc = false
        #     if (int.TryParse(resp, out var data))
        #     {
        #         if ((data & 0x1) == 1)
        #         {
        #             power = true
        #         }
        #         if (((data >> 1) & 0x1) == 1)
        #         {
        #             oc = true
        #         }
        #         //if (((data >> 2) & 0x1) == 1)
        #         //{
        #         //    pol = true
        #         //}
        #         //if (((data >> 3) & 0x1) == 1)
        #         //{
        #         //    irig = true
        #         //}
        #     }

        #     return new SensorStatus(power, oc)
        # }

        def get_sensor_timestamp(self, sensor, toLog = True):
            pass

        # def GetSensorTimestamp(int sensor, toLog = True):
        #     var chValue = f"ch{sensor}"
        #     var tempString = f"{WiznetSensorCommands.TIMESTAMP}? {chValue}"
        #     var resp = await Send(tempString, toLog)
        #     try
        #     {
        #         var timeString = resp.Split(new char[] { ':', '.' })
        #         var minutes = int.Parse(timeString[0])
        #         if(minutes > 59) { throw new ArgumentException("No Timestamp") }
        #         var seconds = int.Parse(timeString[1])
        #         if(seconds > 59) { throw new ArgumentException("No Timestamp") }
        #         var micro = int.Parse(timeString[2])
        #         if(micro > 999999) { throw new ArgumentException("No Timestamp") }
        #         var today = DateTime.UtcNow
        #         var thisHour = new DateTime(today.Year, today.Month, today.Day, 12, 0, 0)
        #         //var noon = new DateTime(today.Year, today.Month, today.Day, 12, 12, 0)
        #         var calcTicks = (long)(micro * 10 + (seconds + 60 * minutes) * 10e6)// + minutes * 6000000
        #         //var calcTicks = (noon.Ticks - thisHour.Ticks) / 12
        #         //var combined = new DateTime(now.Year, now.Month, now.Day, now.Hour, minutes, seconds, micro)
        #         var combined = new DateTime(thisHour.Ticks + calcTicks)
        #         return combined.ToString()
        #     }
        #     catch(FormatException)
        #     {
        #         return "Bad Format"
        #     }
        #     catch(ArgumentException ex)
        #     {
        #         return ex.Message
        #     }
            
        # }


    def to_channel(self, sensor):
        try:
            return f"ch{int(sensor)}"
        except:
            return sensor

    def to_onoff_string(self, setting):
        try:
            return on_off.on_off_to_string(setting)
        except:
            return setting

class TriggerSelectOptions(Enum):
    NONE = 0, 
    FMH = 1, 
    FMV = 2, 
    FMB = 3, 
    ZTCH = 4,
    ZTCV = 5, 
    ZTCB = 6, 
    POLH = 7, 
    POLV = 8, 
    SFMH = 9, 
    SFMV = 10, 
    SZTCH = 11, 
    SZTCV = 12, 
    BFMH = 13, 
    BFMV = 14, 
    BZTCH = 15, 
    BZTCV = 16, 
    SFMSBLKH = 17, 
    SFMSBLKV = 18, 
    SZTCSBLKH = 19, 
    SZTCSBLKV = 20, 

class TriggerState(Enum):
    Reset = 0,
    Ready = 1,
    Triggered = 2,
    Pulse = 3,
    Continuous = 4
