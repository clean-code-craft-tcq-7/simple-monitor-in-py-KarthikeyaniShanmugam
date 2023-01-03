from printer import print_abnormal_state
class SocChecker():
    def __init__(self) -> None:
        self.soc_state = True
        self.soc_minimum_threshold = 20
        self.soc_maximum_threshold = 80
    def check_battery_soc_abnormality(self,soc):
        if soc < self.soc_minimum_threshold or soc > self.soc_maximum_threshold:
            print_abnormal_state('State of Charge')
            self.soc_state = False
        return self