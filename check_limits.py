from check_temperature_limits import *
from check_soc_limits import *
from check_charge_rate_limits import *

def battery_is_ok(temperature, soc, charge_rate):
    temperatureChecker = TemperatureChecker()
    socChecker = SocChecker()
    chargerateChecker = ChargeRateChecker()    
    temperatureChecker.check_battery_temperature_abnormality(temperature)
    socChecker.check_battery_soc_abnormality(soc)
    chargerateChecker.check_charge_rate_abnormality(charge_rate)
    
    return (temperatureChecker.temperature_state and socChecker.soc_state and chargerateChecker.charge_rate_state)

