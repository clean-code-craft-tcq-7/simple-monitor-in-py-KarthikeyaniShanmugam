from printer import *
from warning_value_calculator import calculate_warning
from configuration_warning import *

class TemperatureChecker():
    def __init__(self) -> None:
        self.temperature_state = True    
        self.temperature_minimum_threshold = 0
        self.temperature_maximum_threshold = 45

        self.minimum_warning_value = self.temperature_minimum_threshold + calculate_warning(self.temperature_maximum_threshold)
        self.maximum_warning_value = self.temperature_maximum_threshold - calculate_warning(self.temperature_maximum_threshold)

        self.minimum_warning = False
        self.maximum_warning = False
    
    def check_minimum_warning(self,temperature):
        if temperature > self.temperature_minimum_threshold and temperature <= self.minimum_warning_value:
            self.minimum_warning = True            

    def check_maximum_warning(self,temperature):
        if temperature > self.maximum_warning_value and temperature <= self.temperature_maximum_threshold:
            self.maximum_warning = True            
   
    def print_minimum_warning(self):
        if temperature_warning and self.minimum_warning:
            print_minimum_warning('Temperature')

    def print_maximum_warning(self):            
        if temperature_warning and self.maximum_warning:
            print_maximum_warning('Temperature')

    def check_battery_temperature_abnormality(self,temperature):
        self.check_minimum_warning(temperature)
        self.check_maximum_warning(temperature)
        self.print_minimum_warning()
        self.print_maximum_warning()

        if (temperature < self.temperature_minimum_threshold or temperature > self.temperature_maximum_threshold):
            print_abnormal_state('Temperature')
            self.temperature_state = False
        return self
