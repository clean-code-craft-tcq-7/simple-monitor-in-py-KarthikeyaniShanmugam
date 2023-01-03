from check_charge_rate_limits import ChargeRateChecker

if __name__ == '__main__':
    chargerateChecker = ChargeRateChecker()
    chargerateChecker.check_charge_rate_abnormality(0.9)
    chargerateChecker.check_charge_rate_abnormality(0.2)
    chargerateChecker.check_charge_rate_abnormality(0.8)
    chargerateChecker.check_charge_rate_abnormality(-1)
    chargerateChecker.check_charge_rate_abnormality(1.456)
    chargerateChecker.check_charge_rate_abnormality(-100)
    chargerateChecker.check_charge_rate_abnormality(100)