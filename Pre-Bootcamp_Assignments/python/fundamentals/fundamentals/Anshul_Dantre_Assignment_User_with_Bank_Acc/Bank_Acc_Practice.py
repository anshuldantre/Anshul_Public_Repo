class User:
    acc_list = []
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = {"checking": BankAccount(interest_rate=0.02, balance=200),
                        "saving": BankAccount(interest_rate=0.02, balance=1500)
                        }

    def display_user_balance(self):
        print(f'user {self.name}, checking balance = {self.account["checking"].balance}')
        print(f'user {self.name}, saving balance = {self.account["saving"].balance}')
        return self

    def make_deposit(self, amount, acc_type):
        self.account[acc_type].deposit(amount)
        return self

    def do_withdrawal(self, amount, acc_type):
        self.account[acc_type].withdraw(amount)
        return self

    def transfer_money(self, amount, other_user, acc_type):
        self.do_withdrawal(amount, acc_type)
        other_user.make_deposit(amount, acc_type)
        return self

class BankAccount:
    def __init__(self, interest_rate, balance):
        self.interest_rate = interest_rate
        self.balance = balance

    @staticmethod
    def withdrawal_allowed(balance, amount):
        if balance - amount > 0:
            return True
        else:
            return False

    def deposit(self, amount) :
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


# print(user1.account["checking"].balance)
# user1.make_deposit(50,"checking").make_deposit(700,"saving").display_user_balance()
# user2.do_withdrawal(5000,"checking").display_user_balance()

user1.display_user_balance()
user2.display_user_balance()
print('********************************')
user1.transfer_money(25, user2, "checking").display_user_balance()
print('********************************')
user2.display_user_balance()