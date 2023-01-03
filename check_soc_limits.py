from printer import *
from warning_value_calculator import calculate_warning
from configuration_warning import *

class SocChecker():
    def __init__(self) -> None:
        self.soc_state = True
        self.soc_minimum_threshold = 20
        self.soc_maximum_threshold = 80

        self.minimum_warning_value = self.soc_minimum_threshold + calculate_warning(self.soc_maximum_threshold)
        self.maximum_warning_value = self.soc_maximum_threshold - calculate_warning(self.soc_maximum_threshold)

        self.minimum_warning = False
        self.maximum_warning = False
    def check_minimum_warning(self,soc):
        if soc > self.soc_minimum_threshold and soc <= self.minimum_warning_value:
            self.minimum_warning = True            
    
    def check_maximum_warning(self,soc):
        if soc > self.maximum_warning_value and soc <= self.soc_maximum_threshold:
            self.maximum_warning = True
            

    def print_minimum_warning(self):
        if soc_warning and self.minimum_warning:
            print_minimum_warning('State of Charge')

    def print_maximum_warning(self):            
        if soc_warning and self.maximum_warning:
            print_maximum_warning('State of Charge')    
            
    def check_battery_soc_abnormality(self,soc):
        self.check_minimum_warning(soc)
        self.check_maximum_warning(soc)
        self.print_minimum_warning()
        self.print_maximum_warning()
        if soc < self.soc_minimum_threshold or soc > self.soc_maximum_threshold:
            print_abnormal_state('State of Charge')
            self.soc_state = False
        return self
