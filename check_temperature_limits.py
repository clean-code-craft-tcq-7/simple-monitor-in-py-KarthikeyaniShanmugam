from printer import *
from warning_value_calculator import calculate_warning
from configuration_warning import *

class TemperatureChecker():
    def __init__(self) -> None:
        self.temperature_state = True    
        self.temperature_minimum_threshold = 0
        self.temperature_maximum_threshold = 45

        self.minimum_warning = self.temperature_minimum_threshold + calculate_warning(self.temperature_maximum_threshold)
        self.maximum_warning = self.temperature_maximum_threshold - calculate_warning(self.temperature_maximum_threshold)

    def check_battery_temperature_abnormality(self,temperature):
        if temperature_warning:
            if temperature > self.temperature_minimum_threshold and temperature <= self.minimum_warning:
                print_minimum_warning('Temperature')

            if temperature > self.maximum_warning and temperature <= self.temperature_maximum_threshold:
                print_maximum_warning('Temperature')

        if (temperature < self.temperature_minimum_threshold or temperature > self.temperature_maximum_threshold):
            print_abnormal_state('Temperature')
            self.temperature_state = False
        return self
