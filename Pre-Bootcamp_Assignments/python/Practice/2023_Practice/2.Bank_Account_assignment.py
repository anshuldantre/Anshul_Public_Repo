# The BankAccount class should have a balance. When a new BankAccount instance is created, if an amount is given, the balance of the account should initially be set to that amount;
#  otherwise, the balance should start at $0. The account should also have an interest rate in decimal format. For example, a 1% interest rate would be saved as 0.01. 
# The interest rate should be provided upon instantiation. (Hint: when using default values in parameters, the order of parameters matters!)

# Create a BankAccount class with the attributes interest rate and balance
class BankAccount:
    bank_accounts = []
    def __init__(self, int_rate, balance=0):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.bank_accounts.append(self)

# Add a deposit method to the BankAccount class
# deposit(self, amount) - increases the account balance by the given amount
    def deposit(self, amount):
        self.balance += amount
        return self

# Add a withdraw method to the BankAccount class
# withdraw(self, amount) - decreases the account balance by the given amount if there are sufficient funds; if there is not enough money, 
# print a message "Insufficient funds: Charging a $5 fee" and deduct $5
    def withdraw(self, amount):
        if amount > self.balance:
            self.balance -= 5
            print(f"Insufficient funds: Charging a $5 fee")
            return self
        self.balance -= amount
        return self

# Add a display_account_info method to the BankAccount class
# display_account_info(self) - print to the console: eg. "Balance: $100"
    def display_account_info(self):
        print(f'Balance ${self.balance}')
        return self

# Add a yield_interest method to the BankAccount class
# yield_interest(self) - increases the account balance by the current balance * the interest rate (as long as the balance is positive)
    def yield_interest(self):
        if self.balance > 0:
            self.balance *= self.int_rate
        return self


    @classmethod
    def all_accounts(cls):
        for account in cls.bank_accounts:
            print(f'My interest rate is {account.int_rate} and the total balance is {account.balance}')

# Create 2 accounts
anshul_acc = BankAccount(2,200)
sharda_acc = BankAccount(1,500)

# print(f'My interest rate is {sharda_acc.int_rate} and the total balance is {sharda_acc.balance}')

# To the first account, make 3 deposits and 1 withdrawal, then yield interest and display the account's info all in one line of code (i.e. chaining)
anshul_acc.deposit(100).deposit(200).deposit(500).withdraw(400).display_account_info()

# To the second account, make 2 deposits and 4 withdrawals, then yield interest and display the account's info all in one line of code (i.e. chaining)
sharda_acc.deposit(100).deposit(200).withdraw(15).withdraw(20).withdraw(25).withdraw(30).display_account_info()

# NINJA BONUS: use a classmethod to print all instances of a Bank Account's info
BankAccount.all_accounts()