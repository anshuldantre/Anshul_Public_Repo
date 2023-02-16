class User:
    def __init__(self,first_name, email, account):
        self.first_name = first_name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)

    def user_balance(self):
        self.account.deposit(100)
        print(self.account.balance)

class BankAccount:
    bank_accounts = []
    def __init__(self, int_rate, balance=0):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.bank_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if amount > self.balance:
            self.balance -= 5
            print(f"Insufficient funds: Charging a $5 fee")
            return self
        self.balance -= amount
        return self

    def display_account_info(self):
        print(f'Balance ${self.balance}')
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance *= self.int_rate
        return self

    @classmethod
    def all_accounts(cls):
        for account in cls.bank_accounts:
            print(f'My interest rate is {account.int_rate} and the total balance is {account.balance}')

anshul_acc = BankAccount(2,200)
sharda_acc = BankAccount(1,500)
anshul_acc.deposit(100).deposit(200).deposit(500).withdraw(400).display_account_info()
sharda_acc.deposit(100).deposit(200).withdraw(15).withdraw(20).withdraw(25).withdraw(30).display_account_info()
BankAccount.all_accounts()