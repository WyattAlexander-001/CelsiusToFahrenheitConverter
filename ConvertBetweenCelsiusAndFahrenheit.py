# -*- coding: utf-8 -*-
"""
Celsius to Fahrenheit

C=>F
(0°C × 9/5) + 32 = 32°F

F=>C
(32°F − 32) × 5/9 = 0°C

"""
def main():

    print('''Are We Converting From Celsius Or Fahrenheit Today?''')
    
    startingValue = input('Type C for Celsius or F for Fahrenheit:\n').lower()
    
     
    if startingValue == "c":
        celsius = float(input('Enter your Celsius Value:\n'))
        celsiusToFahrenheit = (celsius * (9/5)) + 32
        celsiusToFahrenheit = round(celsiusToFahrenheit)
        print(f'{celsiusToFahrenheit}°F')
    elif startingValue == "f":
        fahrenheit = float(input('Enter your Fahrenheit Value:\n'))
        FahrenheitToCelsius = (fahrenheit - 32) * (5/9)
        FahrenheitToCelsius = round(FahrenheitToCelsius)
        print(f'{FahrenheitToCelsius}°C')
    else:
        print('Error Incorrent Value')

    x = input('Try again? Type yes or no\n').lower()
    if x == 'yes':
        main()
    else:
        print('Done')

main()