# We often use Object Oriented Programming for web development because we want to work more efficiently and write less code. In order to achieve better code, 
# we use the 4 pillars of OOP.

# Benefits of using OOP:
# Implements D.R.Y. (Don't Repeat Yourself) code
# Makes our application scalable.
# Makes our code reusable. 
# Makes our applications easily maintainable.

# 1. Encapsulation
# Encapsulation is the idea that we can group code together into objects; hence Object Oriented Programming. 
# We use classes or "coding blue prints" to define what our objects are and how they behave. We encapsulate attributes and methods in our class.
# Example :

class CoffeeM:
    def __init__(self,name):
        self.name = name
        self.water_temp = 200
    def brew_now(self,beans):
        print(f"Using {beans}!")
        print("Brew now brown cow!")
    def clean(self):
        print("Cleaning!")


# 2. Inheritance
# Inheritance is the idea that we pass along attributes and methods from one class into a "sub-class" or child class, and not have to re-write the code to make it work. 
# Child classes can be more specific versions of their Parent class.  Using the key word "super" will call methods
# Example :

class CappuccinoM( CoffeeM ):
    def __init__(self,name):
        super().__init__(name)
        self.milk = "whole"
    def make_cappuccino(self,beans):
        super().brew_now(beans)
        print("Frothy!!!")



# 3. Polymorphism
# Polymorphism means "many forms", and the idea in OOP is that a Child class can have a different version of a method than the Parent class. 
# In this example the child class of CappuccinoM has a clean method, and so does CoffeeM. Depending on the class, the clean method will do different things.
# Example :

class CappuccinoM( CoffeeM ):
    def __init__(self,name):
        super().__init__(name)
        self.milk = "whole"
    def make_cappuccino(self,beans):
        super().brew_now(beans)
        print("Frothy!!!")
    def clean(self):
        print("Cleaning the froth!")


# 4. Abstraction
# Abstraction is an extension of Encapsulation, and we can hide attributes or methods that a Barista doesnt need to know about, like a CoffeeM. 
# That way the Barista can make a cup of coffee in a simpler manner.
# Example :

class Barista:
    def __init__(self,name):
        self.name = name
        self.cafe = CoffeeM("Cafe")
    def make_coffee(self):
        self.cafe.brew_now()