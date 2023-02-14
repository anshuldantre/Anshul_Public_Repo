# Dictionaries are also iterable
person = {"first":"Anshul", "last":"Dantre", "Age": 39, "dob": "25/02/1984"}
for items in person:
    print(items)

# To get the keys and values for a dictionary when parsing via keys
person = {"first":"Anshul", "last":"Dantre", "Age": 39, "dob": "25/02/1984"}
for keys in person:
    print(person[keys])

# Other methods to iterate through a dictionary
person = {"first":"Anshul", "last":"Dantre", "Age": 39, "dob": "25/02/1984"}
# another way to iterate through the keys
for key in person.keys():
    print(key)

#to iterate through the values
person = {"first":"Anshul", "last":"Dantre", "Age": 39, "dob": "25/02/1984"}
for val in person.values():
    print(val)

#to iterate through both keys and values
person = {"first":"Anshul", "last":"Dantre", "Age": 39, "dob": "25/02/1984"}
for key, val in person.items():
    print(key, " = ", val)