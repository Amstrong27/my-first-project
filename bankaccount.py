class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = max(0, balance)  # prevent negative balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return False
        self.balance += amount
        print(f"Deposit of {amount} successful.")
        return True

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        if amount > self.balance:
            print("Insufficient balance.")
            return False
        self.balance -= amount
        print(f"Withdrawal of {amount} successful.")
        return True

    def display_balance(self):
        print(f"Account Number: {self.account_number}")
        print(f"Current Balance: {self.balance}")

if __name__ == "__main__":
    account1 = BankAccount("123456789", 1000)
    account2 = BankAccount("987654321", 500)

    account1.display_balance()
    account1.deposit(500)
    account1.display_balance()
