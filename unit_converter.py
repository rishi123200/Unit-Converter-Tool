# Unit Converter Tool

def length_converter():
    print("\nLength Conversion")
    meters = float(input("Enter value in meters: "))
    print("Kilometers =", meters / 1000)
    print("Centimeters =", meters * 100)

def weight_converter():
    print("\nWeight Conversion")
    kg = float(input("Enter value in kilograms: "))
    print("Grams =", kg * 1000)

def temperature_converter():
    print("\nTemperature Conversion")
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print("Fahrenheit =", fahrenheit)

while True:
    print("\n===== UNIT CONVERTER TOOL =====")
    print("1. Length Conversion")
    print("2. Weight Conversion")
    print("3. Temperature Conversion")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        length_converter()
    elif choice == 2:
        weight_converter()
    elif choice == 3:
        temperature_converter()
    elif choice == 4:
        print("Thank you for using Unit Converter Tool!")
        break
    else:
        print("Invalid Choice! Please try again.")