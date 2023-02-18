class User:
    def __init__(self, name, email, acc_type):
        self.name = name
        self.email = email
        self.account = { 
                        "savings": BankAccount(int_rate = 0.42, balance = 0),
                        "checking": BankAccount(int_rate = 0.42, balance = 0)
                    }

    def make_deposit(self, amount, acc_type):
        self.account[acc_type].deposit(amount)
        return self

    def make_withdrawal(self, amount, acc_type):
        self.account[acc_type].withdraw(amount)
        return self

    def display_user_balance(self):
        print(f'{self.name}, savings account {self.account["savings"].balance}')
        print(f'{self.name}, checking account {self.account["checking"].balance}')

    def transfer_money(self, from_acc, amount):
        if from_acc == "savings":
            User.make_withdrawal(self, amount, "savings")
            User.make_deposit(self, amount, "checking")
        else:
            User.make_withdrawal(self, amount, "checking")
            User.make_deposit(self, amount, "savings")
        return self

class BankAccount:
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance= balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        return self.balance

    def yield_interest(self):
        pass

ansh_user = User("Anshul","abc@abc.com", "savings")
ansh_user = User("Anshul","abc@abc.com", "checking")
ansh_user.make_deposit(100, "savings").make_withdrawal(35, "savings")
ansh_user.make_deposit(200, "checking").make_withdrawal(10, "checking")
ansh_user.display_user_balance()
ansh_user.transfer_money("savings", 10)
ansh_user.display_user_balance()