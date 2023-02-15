class User: # Class name is singular and first alphabet is capatilized
    
    # Consructor Function !!!...Creates the instance of an object
    def __init__(self, first_name, last_name, age):
        pass
    # __init__ is the magic contructor method built in python
    # Self is a representation of an instance of an object. 

# This is how we define instance of a class
michael = User()
anna = User() 

# -------------------------------------------------------------------------------------
class User:
    def __init__(self):
        self.first_name = "Anshul"
        self.last_name = "Dantre"
        self.age = 39

user_anshul = User()
user2 = User()
print(user_anshul.first_name)
print(user2.last_name)

# -------------------------------------------------------------------------------------
# Instance attributes
class Shoe:
    def __init__(self):
        self.brand = "Vans"
        self.type = "Classic Sk8-Hi"
        self.price = 69.99
        self.in_stock = True

skater_shoe = Shoe()
dress_shoe = Shoe()

print(skater_shoe.type)
print(dress_shoe.type)

skater_shoe.type = "Low-Top Trainers"
print(skater_shoe.type)

dress_shoe.type = "Ballet Flats"
print(dress_shoe.type)

# -------------------------------------------------------------------------------------
# Instance attibutes as arguments
class Shoe:
    def __init__(self, brand, type, price):
        self.brand = brand
        self.type = type
        self.price = price
        self.in_stock = True

skater_shoe = Shoe("Vans", "Low Top Trainers", 59.99)
dress_shoe = Shoe("Jack & Jill Bootery", "Ballet Flats", 29.99)

print(skater_shoe.type)
print(dress_shoe.type)

# -------------------------------------------------------------------------------------
# Methods within a class
class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def greeting(self):
        print("Greetings " + self.first_name)

user_anshul = User("Anshul", "Dantre", 39)
print(user_anshul.first_name)
user_anshul.greeting()

# -----------------------------------------------------------------------------------------
class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_reward_member = False
        self.gold_card_points = 0

    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_reward_member)
        print(self.gold_card_points)

    def enroll(self):
        if self.is_reward_member:
            return "Already a member"
        else:
            self.is_reward_member = True
            self.gold_card_points = 200
        return "Enrollement Successful"

    def spend_points(self, amount):
        if self.gold_card_points < amount:
            print("Insufficient Balance, cant proceed")
        else:
            self.gold_card_points -= amount

user_anshul = User("Anshul", "Dantre", "anshul.dantre@gmail.com", 39)
user_shradha = User("Shradha", "Tripathi", "shradha.sid@gmail.com", 37)
user_rahul = User("Rahul", "Jain", "Rahul.Jain@gmail.com", 38)

# user_anshul.display_info()
# print("-------------------------------------------------------------------------")
# user_shradha.display_info()
# print("------------------------------------")
print(user_shradha.enroll())
print(user_shradha.enroll())
# user_shradha.display_info()
# print("-------------------------------------------------------------------------")
# user_rahul.display_info()
# print("-------------------------------------------------------------------------")
user_anshul.spend_points(50)
# print("-------------------------------------------------------------------------")
# user_anshul.display_info()
user_shradha.spend_points(80)
print("-------------------------------------------------------------------------")
user_shradha.display_info()
print("-------------------------------------------------------------------------")
user_rahul.spend_points(40)

# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Chaining method: to call multiple methods in a single shot usig a dot notation
# Condition the method shoudl always return self in order for chaining to work

class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_reward_member = False
        self.gold_card_points = 0

    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_reward_member)
        print(self.gold_card_points)
        return self

    def enroll(self):
        if self.is_reward_member:
            print("Already a member")
        else:
            self.is_reward_member = True
            self.gold_card_points = 200
            print("Enrollement Successful")
        return self

    def spend_points(self, amount):
        if self.gold_card_points < amount:
            print("Insufficient Balance, cant proceed")
        else:
            self.gold_card_points -= amount
        return self

user_anshul = User("Anshul", "Dantre", "anshul.dantre@gmail.com", 39)

user_anshul.display_info().enroll().display_info()
print("-----------------------------------------------------------------------------")
user_anshul.spend_points(80).display_info()