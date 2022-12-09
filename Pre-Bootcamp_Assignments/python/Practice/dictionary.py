person = {'first_name':'Anshul','last_name':'Dantre','age':39,'is_organ_donor':True}
print(person)
capitals={}
print(capitals)

capitals['svk']='Bratislava'
capitals['deu']='Berlin'
capitals['dnk']='Copenhagen'
print(capitals)

print(person['age'])


fruit = {"fruit1":"Apple",
"fruit2":"Banana",
"fruit3":"Cucumber"
}
print(fruit)

if "fruit4" not in fruit:
    fruit["fruit4"]= "aaauuuu"
print(fruit)

#del fruit["fruit3"]
val_removed = fruit.pop('fruit3')
print(fruit)
print(val_removed)
print(len(fruit))
print(str(fruit))
print(type(fruit))
#print(fruit.clear())

fruit = {"fruit1":"Apple",
"fruit2":"Banana",
"fruit3":"Cucumber"
}
#print(fruit.get('fruit30'))

fruit2 = {"fruit1":"Apple",
"fruit2":"Banana",
"fruit3":"Cucumber"
}

fruit.update(fruit2)
print(fruit)


person = {'first_name':'Anshul','last_name':'Dantre','age':39,'is_organ_donor':True}
for x in person:
    print(x,person[x])

capitals = {"Washington":"Olympia",
            "California":"Sacramento",
            "Idaho":"Boise",
            "Illinois":"Springfield",
            "Texas":"Austin",
            "Oklahoma":"Oklahoma City",
            "Virginia":"Richmond"}

for x in capitals.keys():
    print(x)

for x in capitals.values():
    print(x)

for x,y in capitals.items():
    print(x,y)

users = [   {"first" : "Anshul", "last":"Dantre"},
            {"first":"Shradha", "last":"Tripathi"},
            {"first":"Rahul", "last":"Jain"},
            {"first":"Komal", "last":"Nahata"}]

resume_data = { "Devlead":["oracle","python","ITAO"],
                "QA":["Manual","automation","deployments"],
                "Audit":["Python","Tableau","Testing"],
                "BA":["Analysis","functional","healthcare"]
}

print(users[2]["last"])
print(resume_data["Devlead"][1])