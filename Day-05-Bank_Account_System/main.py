# BASIC BANK ACCOUNT SYSTEM

class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited amount: ${amount: .2f}. New balance: ${self.__balance: .2f}")
        else:
            print("Deposit amount must be positive means greater than zero.")
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn amount: ${amount: .2f}. New balance: ${self.__balance: .2f}")
        else:
            print("Withdrawal amount must be positive and less than or equal to the current balance")

    def show_balance(self):
        print(f"Account holder: {self.account_holder}, Current balance is: ${self.__balance: .2f}")

    
my_account = BankAccount("Tanisha", 2000000)

my_account.show_balance()
my_account.deposit(50000)
my_account.withdraw(200)