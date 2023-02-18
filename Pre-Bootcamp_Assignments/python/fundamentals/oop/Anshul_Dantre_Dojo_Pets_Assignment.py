# implement __init__( first_name , last_name , treats , pet_food , pet )
# implement the following methods:
# walk() - walks the ninja's pet invoking the pet play() method
# feed() - feeds the ninja's pet invoking the pet eat() method
# bathe() - cleans the ninja's pet invoking the pet noise() method

class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food

    def walk(self):
        self.pet.play()
        return self

    def feed(self):
        self.pet.eat()
        return self

    def bathe(self):
        self.pet.noise()

# ------------------------------------------------------------------------------------------------------------
# implement __init__( name , type , tricks ):
# implement the following methods:
# sleep() - increases the pets energy by 25
# eat() - increases the pet's energy by 5 & health by 10
# play() - increases the pet's health by 5
# noise() - prints out the pet's sound

class Pet:
    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 60
        self.energy = 60

    def sleep(self):
        self.energy += 25
        return self

    def eat(self):
        if len(pet_food_stock) > 0:
            self.energy += 5
            self.health += 10
            food = pet_food_stock.pop()
            print(f"{self.name} just had {food}, new health is {self.health} and energy level is {self.energy}")
        else:
            print("Out of pet food, please rush to a nearby store")
        return self

    def play(self):
        self.health += 5
        print(f"{self.name} just started playing")
        return self

    def noise(self):
        print(f'{self.name} enjoyed the shower making noises')
        return self

pet_food_stock = ["Milk", "Grass", "Apples"]
treats_option = ["Banana", "Watermelon"]

honey = Pet("Honey", "Elephant", ["Stand on two legs", "Shake head & dance", "Pull or Push a Truck"])
Anshul = Ninja("Anshul", "Dantre",treats_option, pet_food_stock, honey)

Anshul.walk().feed().walk().feed().feed().feed().bathe()
