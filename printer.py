from configuration_printer_language import *
def print_abnormal_state(print_item):
    if language == 'en':  # 'en' for english
        print(f"{print_item} is out of range!")
    if language == 'gr': # 'gr' for german
        print(f"{print_item} ist außer Reichweite!")

def print_maximum_warning(print_item):
    if language == 'en':  # 'en' for english
        print(f"{print_item} is approaching maximum value!")
    if language == 'gr': # 'gr' for german
        print(f"{print_item} nähert sich dem Maximalwert!")    

def print_minimum_warning(print_item):
    if language == 'en':  # 'en' for english
        print(f"{print_item} is approaching minimum value!")
    if language == 'gr': # 'gr' for german
        print(f"{print_item} nähert sich dem Mindestwert!")    
