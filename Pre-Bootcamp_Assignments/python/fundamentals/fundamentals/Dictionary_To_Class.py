kevin = {"name": "Kevin Durant", "age": 34, "position": "Small Forward", "team" : "Brooklyn Nets"}

class Player:
    def __init__(self, name, age, position, team):
        self.name = name
        self.age = age
        self.position = position
        self.team = team

player_kevin = Player(kevin["name"], kevin["age"], kevin["position"], kevin["team"])
print(player_kevin.position)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

class Player:
    def __init__(self, player_dict):
        self.name = player_dict["name"]
        self.age = player_dict["age"]
        self.position = player_dict["position"]
        self.team = player_dict["team"]

kevin = {"name": "Kevin Durant", "age":34, "position": "small forward", "team": "Brooklyn Nets"}

# Uncomment the line below to test
player_kevin = Player(kevin)

print(player_kevin.name)
print(player_kevin.age)
print(player_kevin.position)
print(player_kevin.team)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

class Player:
    def __init__(self, player_dict):
        self.dict = player_dict

kevin = {"name": "Kevin Durant", "age":34, "position": "small forward", "team": "Brooklyn Nets"}

# Uncomment the line below to test
player_kevin = Player(kevin)
print(type(player_kevin))

print(player_kevin.dict["name"])
print(player_kevin.dict["age"])
print(player_kevin.dict["position"])
print(player_kevin.dict["team"])