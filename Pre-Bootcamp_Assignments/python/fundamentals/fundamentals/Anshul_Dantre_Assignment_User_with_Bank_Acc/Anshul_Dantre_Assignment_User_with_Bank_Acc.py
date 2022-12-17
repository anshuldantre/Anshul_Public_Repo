class User:
    acc_list = []
    def __init__(self, name, email):
        self.name = name
        self.email = email
        # self.acc_type = acc_type
        self.account = BankAccount(interest_rate=0.02, balance=0)
        User.acc_list.append(self)

    def display_user_balance(self):
        print(f'Name = {self.name}\nemail = {self.email}\nbalance = {self.account.balance}')
        return self

    def make_deposit(self,amount):
        self.account.deposit(amount)
        return self

    def do_withdrawal(self,amount):
        self.account.withdraw(amount)
        return self

class BankAccount:
    def __init__(self, interest_rate, balance):
        self.interest_rate = interest_rate
        self.balance = balance

    @staticmethod
    def withdrawal_allowed(balance,amount):
        if balance - amount > 0:
            return True
        else:
            return False

    def deposit(self,amount):
        self.balance += amount
        return self

    def withdraw(self,amount):
        if BankAccount.withdrawal_allowed(self.balance, amount):
            self.balance -= amount
        else:
            print('Insufficient funds, deducting $5 as Penalty')
            self.balance -= 5
        return self


user1 = User('Anshul Dantre','anshul.dantre@codingdojo.com')
user2 = User('Robert Buckley','robert.buckley@codingdojo.com')
# user1.display_user_balance()
# print((User.acc_list[0].account.interest_rate))

user1.display_user_balance()
print('----------------------------------------')
user1.make_deposit(500).make_deposit(400).make_deposit(300).do_withdrawal(1250).display_user_balance()
print('----------------------------------------')
user2.display_user_balance()

# print('----------------------------------------')
# for i in range(0,len(User.acc_list)):
#     print((User.acc_list[i].name))