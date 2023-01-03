from printer import print_abnormal_state
class ChargeRateChecker():
    def __init__(self) -> None:
        self.charge_rate_state = True
        self.charge_rate_maximum_threshold = 0.8
    def check_charge_rate_abnormality(self,charge_rate):
        if charge_rate > self.charge_rate_maximum_threshold:
            print_abnormal_state('Charge rate')
            self.charge_rate_state = False
        return self