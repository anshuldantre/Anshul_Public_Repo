import random

def bobs_count():
    return(F'Bob you should take in {random.randint(10,33)} animals today')

print(bobs_count())

# Here's the syntax for creating a class that we want to call User:
class User:
    pass

# And here's how we create a new instance of our class:
michael = User()
anna = User()

class Shoe:
    def __init__(self):
        self.brand = 'Adidas'
        self.type = 'tennis shoe'
        self.price = 45.99
        self.stock = True

    def rebrand(self, new_brand):
        self.brand=new_brand

    def sold_out(self):
        self.stock=False
    
    def on_sale(self,percent):
        self.price = self.price * (1-percent)


class User:
    def __init__(self):
        self.first_name='Anshul'
        self.last_name='Dantre'
        self.age=38

user_1 = User()
print(user_1.first_name)
print(user_1.last_name)
print(user_1.age)

user_2 = User()
print(user_2.first_name)
print(user_2.last_name)
print(user_2.age)


class User:
    def __init__(self,first_name,last_name,age):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age

user1 = User('Anshul','Dantre',38)
print(user1.first_name)
print(user1.last_name)
print(user1.age)
user1.first_name='Shradha'
print(user1.first_name)


class User:
    def __init__(self,name,email):
        self.name=name
        self.email=email
    
    def greeting(self):
        print(f"Hello my name is {self.name} and my email is {self.email}")

user1=User('Anshul','anshul.dantre@gmail.com')
user1.greeting()



class Shoe:
    def __init__(self,brand,type,price):
        self.brand = brand
        self.type = type
        self.price = price
        self.in_stock=True

    def shoe_on_sale(self,discount):
        self.price = self.price * (1-discount)

shoe1=Shoe('Adidas','Sports',99.99)
print(f'Brand = {shoe1.brand}, type={shoe1.type}, price={shoe1.price}, in_stock={shoe1.in_stock}')

# shoe1.price = shoe1.price * (1-0.2)
# print(f'Brand = {shoe1.brand}, type={shoe1.type}, price={shoe1.price}, in_stock={shoe1.in_stock}')

shoe1.shoe_on_sale(0.2)
print(f'Brand = {shoe1.brand}, type={shoe1.type}, price={shoe1.price}, in_stock={shoe1.in_stock}')