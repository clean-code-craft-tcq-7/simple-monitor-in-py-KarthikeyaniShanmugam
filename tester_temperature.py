from check_temperature_limits import *
if __name__ == '__main__':
    temperatureChecker = TemperatureChecker()
    temperatureChecker.check_battery_temperature_abnormality(-100)
    temperatureChecker.check_battery_temperature_abnormality(-1)
    temperatureChecker.check_battery_temperature_abnormality(0)
    temperatureChecker.check_battery_temperature_abnormality(23)
    temperatureChecker.check_battery_temperature_abnormality(45)
    temperatureChecker.check_battery_temperature_abnormality(46)
    temperatureChecker.check_battery_temperature_abnormality(1000)
    temperatureChecker.check_battery_temperature_abnormality(-23.678)