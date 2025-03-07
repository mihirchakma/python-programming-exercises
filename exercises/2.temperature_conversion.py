# EXERCISE #2: TEMPERATURE CONVERSION

# convertToCelsius(32)  →  0.0 
# convertToFahrenheit(100)  →  212 

# Use these two formulas for converting between Celsius and Fahrenheit: 
# -> Fahrenheit = Celsius × (9 / 5) + 32 
# -> Celsius = (Fahrenheit - 32) × (5 / 9) 

def convertToFahrenheit(degreesCelsius):
    # Calculate and return the degrees Fahrenheit:
    fahrenheit = degreesCelsius * (9 / 5) + 32
    return fahrenheit

def convertToCelsius(degreesFahrenheit):
    # Calculate and return the degrees Celsius: 
    celsius = (degreesFahrenheit - 32) * (5 / 9)
    return celsius


print(convertToCelsius(0) == -17.77777777777778)
print(convertToCelsius(180) == 82.22222222222223)
print(convertToFahrenheit(0) == 32)
print(convertToFahrenheit(100) == 212)
print(convertToCelsius(convertToFahrenheit(15)) == 15)
