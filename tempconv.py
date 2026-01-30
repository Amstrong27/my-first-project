def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def celsius_to_kelvin(c):
    return c + 273.15

def kelvin_to_celsius(k):
    return k - 273.15


while True:
    print("\nTemperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == "5":
        print("Goodbye!")
        break

    try:
        temp = float(input("Enter the temperature: "))

        if choice == "1":
            print(f"Result: {celsius_to_fahrenheit(temp):.2f} °F")
        elif choice == "2":
            print(f"Result: {fahrenheit_to_celsius(temp):.2f} °C")
        elif choice == "3":
            print(f"Result: {celsius_to_kelvin(temp):.2f} K")
        elif choice == "4":
            print(f"Result: {kelvin_to_celsius(temp):.2f} °C")
        else:
            print("Invalid choice.")

    except ValueError:
        print("Please enter a valid number.")
