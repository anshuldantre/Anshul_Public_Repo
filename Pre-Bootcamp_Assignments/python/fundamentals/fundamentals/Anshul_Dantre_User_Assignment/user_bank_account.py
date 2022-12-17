class User:
    def __init__(self,first_name,last_name,email,age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
        self.account = BankAccount (int_rate = 0.02, balance = 0)

    #display_info(self) - Have this method print all of the users' details on separate lines
    def display_info(self):
        print(f'first_name = {self.first_name}\nlast_name = {self.last_name}\nemail = {self.email}\nage = {self.age}\nis_rewards_member = {self.is_rewards_member}\ngold_card_points = {self.gold_card_points}')

    #enroll(self) - Have this method change the user's member status to True and set their gold card points to 200.
    def enroll(self):
        if self.is_rewards_member == True:
            print('User already a member')
            a = False
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
            a = True
        return a

    #spend_points(self, amount) - have this method decrease the user's points by the amount specified.
    def spend_points(self, amount):
        if self.gold_card_points > amount:
            self.gold_card_points = self.gold_card_points - amount
        else:
            print('Insufficient points for deduction')
    
    def example_method(self):
        self.account.with_draw(100)
        print(self.account.balance)


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


user1 = User('Anshul','Dantre','anshul.dantre@codingdojo.com',39)
user2 = User('Lionel','Messi','Lionel.Messi@Argentina.com',37)
user3 = User('Cristiano','Ronaldo','Cristiano.Ronaldo@Portugal.com',35)

user1.display_info() 
# user2.display_info()
# user3.display_info()
print('------------------------------------------------------------------------------------------')
# user1.spend_points(50)
# is_user_member = user2.enroll()
# print(is_user_member)
# user2.spend_points(80)
# print('------------------------------------------------------------------------------------------')
# user1.display_info()
# user2.display_info()
# user3.display_info()
# print('------------------------------------------------------------------------------------------')
# is_user_member = user2.enroll()
# print(is_user_member)
# user3.spend_points(40)
# print('------------------------------------------------------------------------------------------')

user1.example_method()

# AnshulsAccount = BankAccount(1.99,42000)
# ShradhasAccount = BankAccount(0,45000)

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

# print('--------------------------------')
# print(AnshulsAccount.balance)
# AnshulsAccount.with_draw(42000)
# print(AnshulsAccount.balance)