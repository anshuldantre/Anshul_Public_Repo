# Another kind of relationship between classes involves inheritance, which is defining a new class based on another class. In other words, it allows one class to take on the 
# attributes and methods from another class with little additional code. This reuse of code results in reduced redundancy and complexity, which we as developers love! 
# The derived classes (also referred to as child or sub classes) can override or extend the functionality of base classes (or parent or super classes).
# Let's consider our BankAccount class from the previous OOP chapter. What if we were told users could have both checking accounts and retirement accounts? There are a lot of things 
# these two types of accounts have in common, but there are some attributes and methods that might differ between the two.
# One way to make a distinction between account types would be to add an attribute of account_type to our BankAccount class. Then in each of our methods, we would have a series of 
# conditional statements that would determine how the method would actually run. But this can get pretty clunky and hard to manage.
# If we go to the other extreme and just create two separate classes, we might end up with something like this:

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

class CheckingAccount:
    def __init__(self, int_rate, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        pass

    def withdraw(self, amount):
        pass

    def write_check(self,amount):
        pass

    def display_account_info(self):
        pass

class RetirementAccount:
    def __init__(self, int_rate, is_roth, balance=0):
        self.int_rate = int_rate
        self.balance = balance
        self.is_roth = is_roth

    def deposit(self, amount):
        # code - assess tax if necessary
        pass

    def withdraw(self, amount):
        # code - assess penalty if necessary
        pass

    def display_account_info(self):
        # code
        pass

# ----------------------------------------------------------------------------------------------------------------------------
# Still, this feels a little repetitive. Inheritance provides a balance between these two options--it allows us to have one parent class that holds the attributes and methods 
# that are common between the new classes. In turn, each child class will only contain what is unique to that class:

class CheckingAccount(BankAccount):
    pass

class RetirmenetAccount(BankAccount):
    pass

# Would you believe that (assuming the BankAccount class is complete) with just the inclusion of the parent class in parentheses, both the CheckingAccount and 
# RetirementAccount classes both have all the attributes and functionality of the parent class? Amazing! Now we just need to figure out how to add the differences, while 
# maintaining what we need from the parent class.
# -------------------------------------------------------------------------------------------------------------------------------

# Here's what we want our RetirementAccount __init__ method to do, and what our parent BankAccount class __init__ method does:
class RetirementAccount(BankAccount):
    def __init__(self, int_rate, is_roth, balance=0):
        self.int_rate = int_rate
        self.is_roth = is_roth
        self.balance = balance
    
class BankAccount:
    def __init__(self, int_rate, balance=0):
        self.int_rate = int_rate
        self.balance = balance
    
# Do you see how the parent class already does 2 of the 3 lines we're trying to execute in our RetirementAccount class? Let's utilize the parent's functionality for this method. 
# To indicate we are trying to use the parent's methods, we call on it with the keyword super. From there, we can call on any of the parent's methods:

class RetirementAccount(BankAccount):
    def __init__(self, int_rate, is_roth, balance=0):
        super().__init__(int_rate, balance)
        self.is_roth = is_roth

class BankAccount:
    def __init__(self, int_rate, balance=0):
        self.int_rate = int_rate
        self.balance = balance

# ----------------------------------------------------------------------------------------------------------------------------------
# The first line in our RetirementAccount __init__ method allows the parent to manage the setting of int_rate and balance. The only line we need to add is to set 
# the is_roth attribute, since this is unique to the RetirementAccount class.
# Let's look at another example. Suppose we wanted to add some logic to our withdraw method.

class ReitrementAccount(BankAccount):
    def withdraw(self, amount, is_yearly):
        if is_yearly:
            amount = amount * 1.10
        if (self.balance - amount) > 0:
            self.balance -= amount
        else:
            print("Insufficient Funds")
        return self

class BankAccount():
    def withdraw(self, amount):
        if (self.balance - amount) > 0:
            self.balance -= amount
        else:
            print("Insufficient Funds")
        return self

# Hopefully you recognize the repetitiveness here and want to reduce it! So let's call on the parent to do the part of the code that is the same:
class RetirementAccount:
    def withdraw(self, amount, is_yearly):
        if is_yearly:
            amount = amount * 1.10
            super().withdraw(amount)
        return self