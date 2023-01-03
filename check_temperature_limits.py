from printer import print_abnormal_state
class TemperatureChecker():
    def __init__(self) -> None:
        self.temperature_state = True    
        self.temperature_minimum_threshold = 0
        self.temperature_maximum_threshold = 45
    def check_battery_temperature_abnormality(self,temperature):
        if (temperature < self.temperature_minimum_threshold or temperature > self.temperature_maximum_threshold):
            print_abnormal_state('Temperature')
            self.temperature_state = False
        return self