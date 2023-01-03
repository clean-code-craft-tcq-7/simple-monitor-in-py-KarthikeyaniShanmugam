from printer import *
from warning_value_calculator import calculate_warning
from configuration_warning import *
class ChargeRateChecker():
    def __init__(self) -> None:
        self.charge_rate_state = True
        self.charge_rate_maximum_threshold = 0.8
        self.maximum_warning_value = self.charge_rate_maximum_threshold - calculate_warning(self.charge_rate_maximum_threshold)
        self.maximum_warning = False
    def check_maximum_warning(self,charge_rate):
        if charge_rate > self.maximum_warning_value and charge_rate <= self.charge_rate_maximum_threshold:
            self.maximum_warning = True

    def print_warning(self):
        if charge_rate_warning and self.maximum_warning:
            print_maximum_warning('Charge rate')
        
    def check_charge_rate_abnormality(self,charge_rate):
        self.check_maximum_warning(self,charge_rate)
        if charge_rate > self.charge_rate_maximum_threshold:
            print_abnormal_state('Charge rate')
            self.charge_rate_state = False
        return self
