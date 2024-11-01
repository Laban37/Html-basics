# These fuctions converts temps sfrom one scale to another

def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


def celsius_to_kelvin(celsius):
    return celsius + 273.15


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5 / 9 + 273.15


def kelvin_to_celsius(kelvin):
    return kelvin - 273.15


def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9 / 5 + 32

# checks if the temp is valid for given scale
def is_valid_temperature(temp, scale):
    return (
            (scale == "C" and temp >= -273.15) or
            (scale == "F" and temp >= -459.67) or
            (scale == "K" and temp >= 0)
    )

#
def convert_temperature(temp, from_scale, to_scale):
    if not is_valid_temperature(temp, from_scale):
        return "Invalid temperature value for the given scale."

    conversions = {
        ("C", "F"): celsius_to_fahrenheit,
        ("C", "K"): celsius_to_kelvin,
        ("F", "C"): fahrenheit_to_celsius,
        ("F", "K"): fahrenheit_to_kelvin,
        ("K", "C"): kelvin_to_celsius,
        ("K", "F"): kelvin_to_fahrenheit,
    }

    return conversions.get((from_scale, to_scale), lambda t: "Invalid conversion")(temp)


def temperature_conversion_app():
    print("Welcome to the Temperature Conversion App!")

    try:
        temp = float(input("Enter the temperature you want to convert: "))
    except ValueError:
        print("Invalid input. Please enter a numeric temperature.")
        return

    from_scale = input("Enter the current scale (C, F, K): ").upper()
    to_scale = input("Enter the target scale (C, F, K): ").upper()

    if from_scale not in {"C", "F", "K"} or to_scale not in {"C", "F", "K"}:
        print("Invalid scale input. Please use 'C', 'F', or 'K' only.")
        return

    result = convert_temperature(temp, from_scale, to_scale)
    if isinstance(result, str):  # Error message
        print(result)
    else:
        print(f"The temperature in {to_scale} is: {result:.2f}")


# Run the app
temperature_conversion_app()
