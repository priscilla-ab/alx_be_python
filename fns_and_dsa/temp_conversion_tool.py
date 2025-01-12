# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """Convert a temperature from Fahrenheit to Celsius."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert a temperature from Celsius to Fahrenheit."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        # Prompt the user for input
        temperature = float(input("Enter the temperature to convert: "))
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == "C":
            converted = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted}°F")
        elif unit == "F":
            converted = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted}°C")
        else:
            raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

