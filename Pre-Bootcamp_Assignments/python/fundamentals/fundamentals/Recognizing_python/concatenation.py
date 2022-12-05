first_name = "Anshul"
last_name = "Dantre"

full_name = first_name + ' ' + last_name
print(full_name)

age = 39
#print('My name is '+ full_name)
print('My name is',full_name,'.')
#print('My name is '+ full_name + ' and my age is ' + str(age))

print ('My name is ',full_name,'and my age is',age)


user_input = '35'
total = 15
#total = total + user_input
total = total + int(user_input)
print(total)

print(f'My first name is {first_name} and Last name is {last_name}. I am {age} years old')

print('My First name is {} and Last name is {}. I am {} years old'.format(first_name, last_name, age))


hw = "Hello %s" % "World"
print(hw)
py = "I love Python %d" % 3
print(py)
print (hw, py)

x = "Hello World"
print(x.title())

string = "anshul dantre"
print(string.upper())

string = "ANSHUL DANTRE"
print(string.lower())

string = "ANSHUL DANTRE is my name. Is that so Anshul Dantre. Did you just say Anshul Dantre"
print(string.count("Anshul Dantre"))

string = "ANSHUL DANTRE is my name. Is that so Anshul Dantre. Did you just say Anshul Dantre"
print(string.split("Anshul Dantre"))

string = "ANSHUL DANTRE is my name. Is that so Anshul Dantre. Did you just say Anshul Dantre"
print(string.find("Anshul Dantre"))

5+5