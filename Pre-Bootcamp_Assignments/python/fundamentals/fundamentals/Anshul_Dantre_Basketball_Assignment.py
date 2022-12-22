players = [
    {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "small forward", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
    },
    {
    	"name": "Kyrie Irving", 
    	"age":32, "position": "Point Guard", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Damian Lillard", 
    	"age":33, "position": "Point Guard", 
    	"team": "Portland Trailblazers"
    },
    {
    	"name": "Joel Embiid", 
    	"age":32, "position": "Power Foward", 
    	"team": "Philidelphia 76ers"
    },
    {
    	"name": "", 
    	"age":16, 
    	"position": "P", 
    	"team": "en"
    }
]

kevin = {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "small forward", 
    	"team": "Brooklyn Nets"
    }

jason = {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
    }

kyrie = {
    	"name": "Kyrie Irving", 
    	"age":32, 
        "position": "Point Guard", 
    	"team": "Brooklyn Nets"
    }

my_player_list = []

class Player_old:
    def __init__(self, name, age, position, team):
        self.name = name
        self.age = age
        self.position = position
        self.team = team

class Player:
    def __init__(self, player_detail):
        self.player_dict = player_detail
    
    @classmethod
    def get_team(cls, team_list):
        new_team_list = []
        for folks in team_list:
            new_team_list.append(cls(folks))
        return new_team_list


player_kevin = Player(kevin)
print(player_kevin.player_dict["name"])
print(player_kevin.player_dict["age"])
print(player_kevin.player_dict["position"])
print(player_kevin.player_dict["team"])
print("-----------------------------------------------------")
player_jason = Player(jason)
print(player_jason.player_dict["name"])
print(player_jason.player_dict["age"])
print(player_jason.player_dict["position"])
print(player_jason.player_dict["team"])
print("-----------------------------------------------------")
player_kyrie = Player(kyrie)
print(player_kyrie.player_dict["name"])
print(player_kyrie.player_dict["age"])
print(player_kyrie.player_dict["position"])
print(player_kyrie.player_dict["team"])
print("-----------------------------------------------------\n")
my_player_list = Player.get_team(players)
for i in range(0,len(my_player_list)):
    print("*********************")
    print(my_player_list[i].player_dict["name"])