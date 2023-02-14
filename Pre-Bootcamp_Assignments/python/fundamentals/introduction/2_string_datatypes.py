# String definition and concatenation using a comma or a plus
string1 = "Anshul"
string2 = 'Dantre'
print(string1 + string2)
print('My Name is '+ string1 + string2)
print('My Name is', string1 , string2)

# ------------------------------------------------------------------------------------------------------
# Issues concatenating a string using plus
string1 = "Anshul"
# print(string1 ,'is ' + 39, 'years old') --TypeError: can only concatenate str (not "int") to str
print(string1 ,'is ' + str(39), 'years old')

# ------------------------------------------------------------------------------------------------------
# Type casting when adding a user input string as a number
num1 = 39
num2 = "37"
# total = num1 + num2 -- TypeError: unsupported operand type(s) for +: 'int' and 'str'
total = num1 + int(num2)
print(total)

# ------------------------------------------------------------------------------------------------------
# print mechanisms
# interpolation
string1 = "Anshul"
string2 = 'Dantre'
print(f'Hello my first name is {string1} and last name is {string2}')
# string.format
print('My first name is {} and last name is {}'.format(string1, string2))
# %formatting
print('Hello There, my first name is %s and my last name is %s. I am %d years old.' %(string1, string2, 39))
# Built in string method
print(string1.title(), string2.title())

# ------------------------------------------------------------------------------------------------------
# Commonly used string methods
string = "Hello World, 123"
print(string.upper())
print(string.lower())
print(string.count('o'))
print(string.split('o'))
print(type(string.split('o')))
print(string.isupper())
print(string.islower())
print(string.isdigit())
print(string.isalpha()) # string with spaces retuns zero for this check
print(string.isalnum())
string = "HelloWorld123"
print(string.isalnum())
print(string.endswith('23'))