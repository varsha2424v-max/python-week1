# Temperature Converter

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    while True:
        print("\n--- Temperature Converter ---")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Exit")

        choice = (input("Enter your choice (1/2/3): ")).strip()

        try:
            if choice == '1':
                c = float(input("Enter temperature in celsius: "))
                print(f"Fahrenheit = {celsius_to_fahrenheit(c):.2f}")

            elif choice == '2':
                f = float(input("Enter temperature in Fahrenheit: "))
                print(f"Celsius = {fahrenheit_to_celsius(f):.2f}")

            elif choice == '3':
                print("Thank you!")
                break

            else:
                print("Invalid choice, try again!")

        except ValueError:
            print("❌ Please enter valid number!")

# Run program
main()