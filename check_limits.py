def check_battery_temperature_abnormality(temperature):
  print("inside temperature")
  if (temperature < 0 or temperature > 45):
      print_abnormal_state('Temperature')
      return False
  else:
      return True
def check_battery_soc_abnormality(soc,previous_output):
  print("inside soc")
  if previous_output:
    if soc < 20 or soc > 80:
      print_abnormal_state('State of Charge')
      return False
    else:
      return True
  return False

def check_charge_rate_abnormality(charge_rate,previous_output):
  print("inside charge rate")
  if previous_output:
    if charge_rate > 0.8:
      print_abnormal_state('Charge rate')
      return False
    else:
      return True
  return False

def print_abnormal_state(print_item):
  print(f"{print_item} is out of range!")


def battery_is_ok(temperature, soc, charge_rate):
    return check_charge_rate_abnormality(charge_rate,check_battery_soc_abnormality(soc,check_battery_temperature_abnormality(temperature)))

# def battery_is_ok1(temperature, soc, charge_rate):
#   if temperature < 0 or temperature > 45:
#     print('Temperature is out of range!')
#     return False
#   elif soc < 20 or soc > 80:
#     print('State of Charge is out of range!')
#     return False
#   elif charge_rate > 0.8:
#     print('Charge rate is out of range!')
#     return False

#   return True




if __name__ == '__main__':
  assert(battery_is_ok(25, 70, 0.7) is True)
  assert(battery_is_ok(50, 85, 0) is False)
