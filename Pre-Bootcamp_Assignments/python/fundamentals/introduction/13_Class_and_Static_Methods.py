# Class attributes, class methods & static methods are not tied to the instance of the class, instead they are tied to the class itself
# They are not a part of the contructor __init__, instead they are part of the class definition and outside constructor
# Class attribute defined within class but outside constructor, do not have self attached to it and are shared amongst all instances
# Class Methods defined within class but outside constructor and starts with @ called decorator like @classmethod def method_name(cls) with cls (class) as input
# Static mthods are very loosly coupled with the class and are defined oustide constructor 
#   but within class itself. Defined as @staticmethod def method_name() with no class/instance input

class User:
    user_count = 0

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        User.user_count += 1

    @classmethod
    def print_user_count(cls):
        print(f'The user count is {cls.user_count}')

    def greeting(self):
        print(f"Hello {self.first_name}")

    @staticmethod
    def validate_age(age):
        is_valid=True
        if age < 18:
            is_valid=False
        return is_valid

user_anshul = User("Anshul", "Dantre", 39)
user_shradha = User("Shradha", "Tripathi", 37)
user_rahul = User("Rahul", "Jain", 36)

# This is how we call a member function/method (Specific to each instance/object)
user_anshul.greeting()

# This is how we call a class method (Spcific to a class)
User.print_user_count()

# This is how we call a static method (Not specific to either class or instance/object)
print(User.validate_age(10))
print(User.validate_age(20))

# ---------------------------------------------------------------------------------------------------------------------------
# Class attributes can be changed for an instance or for the entire class

class BankAccount:
    bank_name = "Bank of America"

    def __init__(self, interest_rate, balance):
        self.int_rate = interest_rate
        self.balance = balance
    
acc_anshul = BankAccount(1, 1000)
acc_shradha = BankAccount(2, 2000)
acc_rahul = BankAccount(3, 3000)

print(acc_anshul.bank_name)
print(acc_shradha.bank_name)
print(acc_rahul.bank_name)
print("------------------------------------------------------------------------------------------------------------------------------------------")
acc_anshul.bank_name = "Chase"
acc_shradha.bank_name = "PNC"
acc_rahul.bank_name = "US Bank"
print(acc_anshul.bank_name)
print(acc_shradha.bank_name)
print(acc_rahul.bank_name)
print("-----------------------------------------------------------------------------------------------------------------")
acc_komal = BankAccount(4, 4000)
BankAccount.bank_name = "Wells Fargo"
print(acc_anshul.bank_name)
print(acc_shradha.bank_name)
print(acc_rahul.bank_name)
print(acc_komal.bank_name)
print("---------------------------------------------------------------------------------")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class BankAccount:
    bank_name = "Bank of America"
    all_accounts = []

    def __init__(self, interest_rate, balance):
        self.interest_rate = interest_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

    @classmethod
    def all_balances(cls):
        for account in cls.all_accounts:
            print(f' Total {account.balance} in {BankAccount.bank_name}')

acc_anshul = BankAccount(1, 1000)
acc_shradha = BankAccount(2, 2000)
acc_rahul = BankAccount(3, 3000)

BankAccount.change_bank_name("Bank of Dojo")
BankAccount.all_balances()

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
# Static Methods
# In Python, static methods offer us the opportunity to organize our code in a better way. We could do a simple check to see if the account can be withdrawn from, 
# but what if we want to scale up our application with more logic around this idea? Well then we would have to update everywhere we are making that evaluation, 
# but if we put it in a @staticmethod, then we can update all the checks from one place. And our code becomes a bit more D.R.Y

class BankAccount:
    # ... __init__ goes here
    def with_draw(self,amount):
        # we can use the static method here to evaluate
        # if we can with draw the funds without going negative
        if BankAccount.can_withdraw(self.balance,amount):
            self.balance -= amount
        else:
            print("Insufficient Funds")
        return self
    # static methods have no access to any attribute
    # only to what is passed into it
    @staticmethod
    def can_withdraw(balance,amount):
        if (balance - amount) < 0:
            return False
        else:
            return True