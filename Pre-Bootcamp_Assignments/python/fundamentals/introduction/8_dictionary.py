# Defined with curly brackets {} # Key value pairs # Not indexed by Numbers, access the values with key # can contain nested sequences # list, tuples and dictionaries

people = {}
person = {"first":"Anshul", "last":"Dantre", "Age": 39, "dob": "25/02/1984"}
print(people)
print(person)

# -------------Adding a new value to dictionary--------------------
person = {"first":"Anshul", "last":"Dantre", "Age": 39, "dob": "25/02/1984"}
person["Gender"] = "Male"
person["Married"] = True
person["Kids"] = "Yes"
print(person)

# Difference between list and dictionary while adding a new value
my_list = []
my_dict = {}

# my_list[0] = 1  List cannot be extended like this. use either a extend or an append method to add a new positional element to a list. Existing value can be changed using this
# my_list[0] = 1  #This will lead to an error
my_list.append(1)
my_list.append(2)
my_list[1] = 5

my_dict["Pos_1"] = 1
my_dict["Pos_2"] = 2

print(my_list)
print(my_dict)

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# checking if a key already in dictionary
person = {"first":"Anshul", "last":"Dantre", "Age": 39, "dob": "25/02/1984"}
# person["email"] = "anshul.dantre@gmail.com"

if "email" not in person:
    person["email"] = "first_name.last_name@email.com"

print(person)
# How to access a specific value within a dictionary
print(person["Age"])

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Removing value from a dictionary
person = {"first":"Anshul", "last":"Dantre", "Age": 39, "dob": "25/02/1984"}
print(person)
removed_value = person.pop("Age")
print(person)
print(removed_value)
del person["dob"]
print(person)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Common built in Functions
person = {"name":"Anshul", "surname":"Dantre", "age":39, "dob":"25-Feb-1984"}
print(person)
print(len(person))
print(str(person))
print(type(person))
print(person.clear())
print(person.get("name"))