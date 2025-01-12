FAHRENHEIT_TO_CELSIUS_FACTOR =5/9  
CELSIUS_TO_FAHRENHEIT_FACTOR =9/5

def convert_to_celsius(fahrenheit):
  """Converts a temperature in Fahrenheit to Celsius and returns the result."""
  celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
  return celsius

def convert_to_fahrenheit(celsius):
  """Converts a temperature in Celsius to Fahrenheit and returns the result."""
  fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
  return fahrenheit

def main():
  """Prompts the user for temperature and unit, performs conversion, and displays the result."""
  while True:
    try:
      temperature = float(input("Enter the temperature to convert: "))
      unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper().strip()
      break
    except ValueError:
      print("Invalid temperature. Please enter a numeric value.")

  if unit == 'C':
    converted_temperature = convert_to_fahrenheit(temperature)
    print(f"{temperature}°C is equivalent to {converted_temperature:.2f}°F")
  elif unit == 'F':
    converted_temperature = convert_to_celsius(temperature)
    print(f"{temperature}°F is equivalent to {converted_temperature:.2f}°C")
  else:
    print("Invalid unit. Please enter 'C' or 'F'.")

if _name_ == "_main_":
  main()

