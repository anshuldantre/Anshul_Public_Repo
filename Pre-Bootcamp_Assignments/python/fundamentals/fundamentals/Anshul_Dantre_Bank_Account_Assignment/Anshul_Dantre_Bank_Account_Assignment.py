# The BankAccount class should have a balance. When a new BankAccount instance is created, if an amount is given, the balance of the account should initially be set to that amount; 
# otherwise, the balance should start at $0. The account should also have an interest rate in decimal format. For example, a 1% interest rate would be saved as 0.01. 
# The interest rate should be provided upon instantiation. (Hint: when using default values in parameters, the order of parameters matters!)

class BankAccount:
    acc_list = []
    def __init__(self,balance,interest):
        if balance < 0:
            self.balance = 0
        else:
            self.balance = balance
        self.interest = interest / 100
        acc_list = BankAccount.acc_list.append(self)

    # The class should also have the following methods:
    # deposit(self, amount) - increases the account balance by the given amount
    def deposit(self, amount):
        self.balance += amount
        return self

    # withdraw(self, amount) - decreases the account balance by the given amount if there are sufficient funds; 
    # if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5
    def withdraw(self, amount):
        if (self.balance - amount) <=0:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount
        return self

    # display_account_info(self) - print to the console: eg. "Balance: $100"
    def display_account_info(self):
        print(f'balance = ${self.balance}\ninterest = {self.interest}%')
        return self

    # yield_interest(self) - increases the account balance by the current balance * the interest rate (as long as the balance is positive)
    def yield_interest(self):
        if self.interest > 0:
            self.balance += (self.balance * self.interest)
        return self

    @classmethod
    def print_all_acc(cls):
        print('---------------List of all accounts-----------------')
        for count in cls.acc_list:
            BankAccount.display_account_info(count)

anshul_acc = BankAccount(500,5)
shradha_acc = BankAccount(-500,19)

anshul_acc.deposit(500).deposit(100).deposit(500).yield_interest().display_account_info()
shradha_acc.deposit(500).deposit(500).withdraw(100).withdraw(100).withdraw(100).withdraw(100).yield_interest().display_account_info()
BankAccount.print_all_acc()