class BankAccount:
    bank_name = "First National Dojo"
    all_accounts = []

    def __init__(self,int_rate,balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    @classmethod
    def change_bank_name(cls,name):
        cls.bank_name=name

    @classmethod
    def all_balances(cls):
        sum = 0
        for account in cls.all_accounts:
            sum += account.balance
        return sum

    @staticmethod
    def can_withdraw(balance,amount):
        if balance - amount < 0:
            return False
        else:
            return True

    def with_draw(self,amount):
        if BankAccount.can_withdraw(self.balance,amount):
            self.balance -= amount
        else:
            print("Insuffucient Funds")
        return self

AnshulsAccount = BankAccount(1.99,42000)
ShradhasAccount = BankAccount(0,45000)

# print(AnshulsAccount.bank_name)
# print(ShradhasAccount.bank_name)

# print('--------------------------------')
# ShradhasAccount.bank_name = "W3 School"
# print(AnshulsAccount.bank_name)
# print(ShradhasAccount.bank_name)

# print('--------------------------------')
# BankAccount.bank_name = "W3 School"
# print(AnshulsAccount.bank_name)
# print(ShradhasAccount.bank_name)

# print('--------------------------------')
# BankAccount.change_bank_name('Yes Bank')
# print(AnshulsAccount.bank_name)
# print(ShradhasAccount.bank_name)

# print('--------------------------------')
# total = BankAccount.all_balances()
# print(total)

print('--------------------------------')
print(AnshulsAccount.balance)
AnshulsAccount.with_draw(42000)
print(AnshulsAccount.balance)