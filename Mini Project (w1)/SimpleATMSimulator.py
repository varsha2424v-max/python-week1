# Mini Project
# Simple ATM Simulator

# Balance variable
balance = 5000.0

# User Login
def login():
    correct_pin = "1234"
    attempts = 0

    print("=" * 35)
    print("      Welcome to ATM")
    print("=" * 35)

    while attempts < 3:
        pin = input("Enter your PIN: ")
        if pin == correct_pin:
            print("\n ✅ Login Successful!\n")
            return True
        else:
            attempts += 1
            print(f"❌ Wrong PIN! {3 - attempts} attempts(s) left. ")

    print("\n❌ Too many wrong attempts. Card blocked!")
    return False

# Check Balance
def check_balance():
    print("\n--- Check Balance ---")
    print(f"Your current balance is: Rs.{balance:.2f}")
 

# Deposit Money
def deposit():
    global balance

    print("\n--- Deposit Money ---")
    amount = float(input("Enter amount to deposit: Rs."))

    if amount <= 0:
        print("❌ Amount must be greater than 0!")
    else:
        balance += amount
        print(f"✅ Rs.{amount:.2f} deposited successfully!")
        print(f" New Balance: Rs.{balance:.2f}")

# Withdraw Money
def withdraw():
    global balance

    print("\n--- Withdraw Money ---")
    amount = float(input("Enter amount to withdraw: Rs."))

    if amount <= 0:
        print("❌ Amount must be greater than 0!")
    elif amount > balance:
        print("❌ Insufficient balance!")
        print(f"Available balance: Rs.{balance:.2f}")
    else:
        balance -= amount
        print(f"✅ Rs.{amount:.2f} withdrawn successfully!")
        print(f" New Balance: Rs.{balance:.2f}")

    
# Show Menu
def show_menu():
    print("\n" + "=" * 35)
    print("            ATM MENU")
    print("=" * 35)
    print("  1. Check Balance")
    print("  2. Deposit Money")
    print("  3. Withdraw Money")
    print("  4. Exit")
    print("-" * 35)

def main():
    if login() == False:
        return
    
    while True:
        show_menu()
        choice = input("Choose option (1-4): ")

        if choice == "1":
            check_balance()

        elif choice == "2":
            deposit()
        
        elif choice == "3":
            withdraw()

        elif choice == "4":
            print("\nThank you for using ATM. Goodbye!")
            break

        else:
            print("❌ Invalid option! Enter 1, 2, 3 or 4.")

main()
        
