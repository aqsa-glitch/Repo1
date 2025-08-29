PIN = "1234"

def get_positive_amount(prompt):
    while True:
        try:
            amt = float(input(prompt))
            if amt <= 0:
                print(" Amount must be positive.")
                continue
            return amt
        except ValueError:
            print(" Please enter a valid number.")


def atm_session():
    balance = 0.0  # starting balance
    while True:
        print("\n===== ATM Menu =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            print(f" Current Balance: {balance:.2f}")
        elif choice == "2":
            amt = get_positive_amount("Enter amount to deposit: ")
            balance += amt
            print(f" Deposited {amt:.2f}. New Balance: {balance:.2f}")
        elif choice == "3":
            amt = get_positive_amount("Enter amount to withdraw: ")
            if amt > balance:
                print(" Insufficient funds.")
            else:
                balance -= amt
                print(f" Withdrawn {amt:.2f}. New Balance: {balance:.2f}")
        elif choice == "4":
            print(" Thank you for using the ATM.")
            break
        else:
            print(" Invalid choice! Please try again.")


def main():
    print("===== Welcome to the ATM =====")
    attempts = 3
    while attempts > 0:
        entered = input("Enter PIN: ").strip()
        if entered == PIN:
            print(" PIN correct. Access granted.")
            atm_session()
            return
        else:
            attempts -= 1
            if attempts > 0:
                print(f"❌ Incorrect PIN. Attempts left: {attempts}")
            else:
                print("⛔ Too many incorrect attempts. Card blocked (simulation).")


if __name__ == "__main__":
    main()
