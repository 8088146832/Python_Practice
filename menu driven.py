# Initial balance
balance = 0


# Function to deposit money
def deposit():
    global balance
    amount = float(input("Enter amount to deposit: "))

    if amount > 0:
        balance += amount
        print("Amount deposited successfully.")
        print("Current Balance:", balance)
    else:
        print("Invalid amount!")


# Function to withdraw money
def withdraw():
    global balance
    amount = float(input("Enter amount to withdraw: "))

    if amount > balance:
        print("Insufficient balance!")


    elif amount <= 0:
        print("Invalid amount!")
    else:
        balance -= amount
        print("Amount withdrawn successfully.")
        print("Current Balance:", balance)


# Function to check balance
def check_balance():
    print("Your current balance is:", balance)


# Main program using while loop
while True:
    print("\n===== Banking System Menu =====")
    print("1. Deposit Money")
    print("2. Withdraw Money")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        deposit()
    elif choice == '2':
        withdraw()
    elif choice == '3':
        check_balance()
    elif choice == '4':
        print("Thank you for using our banking system!")
        break
    else:
        print("Invalid choice! Please try again.")