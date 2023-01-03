from check_soc_limits import SocChecker

if __name__ == '__main__':
    socChecker = SocChecker()
    socChecker.check_battery_soc_abnormality(-100)
    socChecker.check_battery_soc_abnormality(19)
    socChecker.check_battery_soc_abnormality(20)
    socChecker.check_battery_soc_abnormality(40)
    socChecker.check_battery_soc_abnormality(80)
    socChecker.check_battery_soc_abnormality(81)
    socChecker.check_battery_soc_abnormality(1000)
    socChecker.check_battery_soc_abnormality(-23.678)
    socChecker.check_battery_soc_abnormality(23)
