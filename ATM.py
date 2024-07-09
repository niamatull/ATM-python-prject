import time

def atm_system():
    print("="*50)
    print(" " * 10 + "Welcome to the ATM")
    print("="*50)
    time.sleep(3)
    print("\nPlease Insert Your Card...\n")
    time.sleep(4)
    balance = 50000
    password = 12345

    try:
        pin = int(input("Please Enter Your PIN Code: "))
    except ValueError:
        print("\nInvalid Input. Please Enter a Numeric PIN.")
        return

    if pin != password:
        print("\nIncorrect PIN. Exiting...")
        return

    while True:
        print("\n" + "="*50)
        print(" " * 15 + "Main Menu")
        print("="*50)
        print("""
        1: Check Balance
        2: Withdraw
        3: Deposit
        4: Exit
        """)

        try:
            option = int(input("Enter Your Choice: "))
        except ValueError:
            print("\nInvalid Input. Please Enter a ")
        if option == 1:
            print(f"\nYour Current Balance is: ${balance}")
            print("="*50)

        elif option == 2:
            try:
                withdraw_amount = int(input("Enter the Amount to Withdraw: $"))
            except ValueError:
                print("\nInvalid Input. Please Enter a Numeric Amount.")
                continue
            print("="*50)

            if withdraw_amount >= balance:
                print("\nInsufficient Balance.")
            else:
                balance -= withdraw_amount
                print(f"\nYou Withdrew: ${withdraw_amount}")
                print(f"Your Updated Balance is: ${balance}")
            print("="*50)

        elif option == 3:
            try:
                deposit_amount = int(input("Enter the Amount to Deposit: $"))
            except ValueError:
                print("\nInvalid Input. Please Enter a Numeric Amount.")
                continue

            balance += deposit_amount
            print(f"\nYou Deposited: ${deposit_amount}")
            print(f"Your Updated Balance is: ${balance}")
            print("="*50)

        elif option == 4:
            print("\nExiting... Thank You for Using the ATM.")
            print("="*50)
            break
        
        else:
            print("\nInvalid Choice. Please Select a Number Between 1 and 4.")
            print("="*50)

if __name__ == "__main__":
    atm_system()
