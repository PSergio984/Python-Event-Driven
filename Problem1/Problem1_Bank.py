class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited:  ₱{amount:.2f}. New balance:  ₱{self.balance:.2f}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew:  ₱{amount:.2f}. New balance:  ₱{self.balance:.2f}.")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def get_balance(self):
        return self.balance

def main():
    account1 = BankAccount(account_holder="Eric Manabat", initial_balance=1000)
    print(f"Welcome to the Bank Account Manager, {account1.account_holder}!")
    print(f"Account starting balance:  ₱{account1.get_balance():.2f}")
    print(f"-----------------------------------")
    while True:
        print("\nWhat would you like to do?")
        print("1. Deposit\n2. Withdraw\n3. Check Balance\n4. Exit")
        choice = input("Enter your choice (1-4): ").strip()
        if choice == '1':
            amount_str = input("Enter amount to deposit: ").strip()
            try:
                amount = float(amount_str)
                account1.deposit(amount)
            except ValueError:
                print("Invalid amount. Please enter a number.")
        elif choice == '2':
            amount_str = input("Enter amount to withdraw: ").strip()
            try:
                amount = float(amount_str)
                account1.withdraw(amount)
            except ValueError:
                print("Invalid amount. Please enter a number.")
        elif choice == '3':
            print(f"Current balance: ₱{account1.get_balance():.2f}")
        elif choice == '4':
            print("Thank you for using the Bank Account Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
main()