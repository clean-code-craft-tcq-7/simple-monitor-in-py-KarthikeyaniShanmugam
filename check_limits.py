class BatteryChecker():
    def __init__(self) -> None:
        self.temperature_state = True
        self.soc_state = True
        self.charge_rate_state = True

    def check_battery_temperature_abnormality(self,temperature):
        if (temperature < 0 or temperature > 45):
            self.print_abnormal_state('Temperature')
            self.temperature_state = False
        return self
    
    def check_battery_soc_abnormality(self,soc):
        if soc < 20 or soc > 80:
            self.print_abnormal_state('State of Charge')
            self.soc_state = False
        return self

    def check_charge_rate_abnormality(self,charge_rate):
        if charge_rate > 0.8:
            self.print_abnormal_state('Charge rate')
            self.charge_rate_state = False
        return self

    def print_abnormal_state(self,print_item):
        print(f"{print_item} is out of range!")
        
def battery_is_ok(temperature, soc, charge_rate):
    batteryChecker = BatteryChecker()
    batteryChecker.check_battery_temperature_abnormality(temperature).check_battery_soc_abnormality(soc).check_charge_rate_abnormality(charge_rate)
    return (batteryChecker.temperature_state and batteryChecker.soc_state and batteryChecker.charge_rate_state)
    

if __name__ == '__main__':
    assert(battery_is_ok(25, 70, 0.7) is True)
    assert(battery_is_ok(50, 85, 0) is False)
    assert(battery_is_ok(100, -1, 0.999) is False)
