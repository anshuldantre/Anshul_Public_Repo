# Often data represented from DB is in the form of a list of dictionaries
# We will be mostly using this nested structure and there is not limit of nesting

my_list = [{"name":"Anshul", "surname":"Dantre", "dob":"25-Feb-1984", "age":39},    # Index 0
            {"name":"Shradha", "surname":"Tripathi"},                               # Index 1
            {"name":"Rahul", "surname":"Jain","Occupation":"Internal Audit"}]       # Index 2

print(my_list[0])
print(my_list[2]["Occupation"])


my_dict = { "name": ["Anshul","Shradha","Rahul"],
            "surname": ["Dantre", "Tripathi", "Jain"],
            "age": [39, 37, 36]
            }
print(my_dict["name"])
print(my_dict["age"][2])

# -------------------------------------------------------------------------------------------------------------------------------
# Multi Level Nesting
# Get me the age of second person in second group

my_nested_structure = [
            { "name": ["Anshul","Shradha"],
            "surname": ["Dantre", "Tripathi"],
            "age": [39, 37]
            },
            { "name": ["Komal","Rahul"],
            "surname": ["Nahata", "Jain"],
            "age": [33, 36]
            },
            { "name": ["Astha","Avinash"],
            "surname": ["Jain", "Singh"],
            "age": [34, 36]
            }
        ]
print(my_nested_structure)
print(my_nested_structure[1]["age"][1])