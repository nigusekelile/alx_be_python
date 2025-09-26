# temp_conversion_tool.py

# ===== Global Conversion Factors =====
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
FREEZING_POINT_FAHRENHEIT = 32  # Constant offset

# ===== Conversion Functions =====
def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius using global factor."""
    return (fahrenheit - FREEZING_POINT_FAHRENHEIT) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using global factor."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + FREEZING_POINT_FAHRENHEIT


# ===== Main Program (User Interaction) =====
try:
    temp_input = input("Enter the temperature to convert: ").strip()

    # Check if numeric (float/int) input
    if not temp_input.replace('.', '', 1).lstrip('-').isdigit():
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    temp_value = float(temp_input)
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if unit == "C":
        converted = convert_to_fahrenheit(temp_value)
        print(f"{temp_value}°C is {converted}°F")
    elif unit == "F":
        converted = convert_to_celsius(temp_value)
        print(f"{temp_value}°F is {converted}°C")
    else:
        raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

except ValueError as e:
    print(e)
