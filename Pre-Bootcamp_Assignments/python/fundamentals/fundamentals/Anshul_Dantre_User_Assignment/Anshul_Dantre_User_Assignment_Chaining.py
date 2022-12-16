class User:
    def __init__(self,first_name,last_name,email,age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    #display_info(self) - Have this method print all of the users' details on separate lines
    def display_info(self):
        print(f'first_name = {self.first_name}\nlast_name = {self.last_name}\nemail = {self.email}\nage = {self.age}\nis_rewards_member = {self.is_rewards_member}\ngold_card_points = {self.gold_card_points}')
        return self

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
        return self

user1 = User('Anshul','Dantre','anshul.dantre@codingdojo.com',39)

# Make 2 more instances of the User class.
user2 = User('Lionel','Messi','Lionel.Messi@Argentina.com',37)
user3 = User('Cristiano','Ronaldo','Cristiano.Ronaldo@Portugal.com',35)


b = user1.enroll()
b = user2.enroll()
b = user3.enroll()
user1.spend_points(20).display_info()
print('------------------------------------------------------------------------------------------')
user2.spend_points(50).display_info()
print('------------------------------------------------------------------------------------------')
user3.spend_points(80).display_info()