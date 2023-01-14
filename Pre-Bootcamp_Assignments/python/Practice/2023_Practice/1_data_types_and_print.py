# either user single or doubel quotes consistently
print("Hello World in double quotes")
print('Hello World in single quotes')

#define basic data type variable
a=10
b='Anshul'
c=True
print(a)
print(b)
print(c)

#define float type variable and use of type function (It is called a function as is not within a class)
a=2.25
print(type(a))

#use of length function. Doesn't work with a int, float or a boolen type attribute
a='Anshul'
b=1.23
c=1
d=True
print(len(a))
# Commented below to show errors
# print(len(b))
# print(len(c))
# print(len(d))


# Composite data types like list, tuples & dictionaries
# to remeber list uses square brackets, tuples uses parantheses and dictionaries uses curly braces
# tuples are immutable (cannot be changed, remains constant once defined)
list_a = [1,2,3]
list_b = ['a','b','c']
list_c = list_a + list_b
print(list_a)
print(list_b)
print(list_c)
print(f'lenght of a={len(list_a)} and b={len(list_b)} and c={len(list_c)}')
print(f'data type of a={type(list_a)}, b={type(list_b)} and c={type(list_c)}')

# You can add two tuples but not change any attirbute
tuple_p = (1,2,3)
tuple_q = ('p','q','r')
print(tuple_p)
print(tuple_q)
print(f'lenght of a={len(tuple_p)} and b={len(tuple_q)}')
print(f'data type of a={type(tuple_p)}, b={type(tuple_q)}')
tuple_r = tuple_p + tuple_q
print(tuple_r)

# You cannot add two dictionaries using a + like we do for tuples or lists
dict_x = {"name":"Anshul", "surname":"Dantre","dob":"25/02/1984"}
dict_y = {"name":"shradha","surname":"Dantre","dob":"10/03/1986"}
print(dict_x)
print(dict_y)
print(f'lenght of a={len(dict_x)} and b={len(dict_y)}')
print(f'data type of a={type(dict_x)}, b={type(dict_y)}')
dict_z = dict_x + dict_y
print(dict_z)

##############################################################################################################
# Adding attributes from composite datatypes
# adding to a list
list_a = [1,2,3]
list_a.append(4) # here we pass the value to be appended to the last position in a list
print(list_a)

# adding to a tuple will fail as its immutable
tuple_q = ('p','q','r')
tuple_q.append('d')
print(tuple_q)

# adding to a list
dict_x = {"name":"Anshul", "surname":"Dantre","dob":"25/02/1984"}
dict_x["gender"]="male"  # here we pass the value to be appended to the last position in a dictionary in square brackets
print(dict_x)

##############################################################################################################
# Removing attributes from composite datatypes
# removing to a list
list_a = [1,2,3]
list_a.pop(1) # here we pass the position of the element to be eliminated from the list in paranthesis (remember its a function call: pop)
print(list_a)

# removing from a tuple will fail as its immutable
tuple_q = ('p','q','r')
tuple_q.pop('b')
print(tuple_q)

# adding to a list
dict_x = {"name":"Anshul", "surname":"Dantre","dob":"25/02/1984"}
dict_x.pop("surname")  # here we pass the key of the element to be eliminated from the dictionary within paranthesis (remember its a function call: pop)
print(dict_x)

# Leanring: Whenever using a function like append or pop always use () paranthesis, but when adding a new element to dictionary use square brackets


##############################################################################################################
# Modifying and printing an existing elements of composite data types
list_a = [1,2,3]
list_a[1]=4 # here we pass the position of the element to be changed within the list in square brackets
print(list_a)
print(list_a[2])

# Modifying a tuple will fail as its immutable, printing of individual elements doable using position
tuple_q = ('p','q','r')
print(tuple_q[2])

# Modifying and printing a specific element within dictionary
dict_x = {"name":"Anshul", "surname":"Dantre","dob":"25/02/1984"}
dict_x["name"]="Shradha"  # here we pass the key of the element to be changed within square brackets
print(dict_x)
# https://www.w3schools.com/python/python_ref_dictionary.asp


# data type conversion
a = 2.5
print(int(a))
b=4
print(float(b))


# random number generator
import random
print(random.randint(2,100))
# https://docs.python.org/3/library/random.html


# various printing types
name = 'Anshul'
print(f'my name is {name}')
print('my name is {} Dantre. How do you do {}'.format(name,name))

a = 39.5
print('my age=',a)

a = 39.5
print('my age is ' + str(a)) # Number to be casted into a string type to be able to concatenate
print('my age is ' + a)


a = 10
b = "20"
print(a + int(b)) # Number to be casted into a integer type to be able to add
print(a+b)


# Built in string methods
a = 'This is just a TEST'
print(a.upper())
print(a.lower())
print(a.count('T'))
print(a.split('a'))
print(a.find('is'))

a = 'This is just a TEST'
print(a.isalnum()) #retuns flase for alphanumeric since there are spaces
a = 'ThisisjustaTEST'
print(a.isalnum())

a = 'This is just a TEST'
print(a.isdigit())
a='1,2,3'
print(a.isdigit())
a='123'
print(a.isdigit())

a = 'This is just a TEST'
print(a.islower())
a = 'this is just a test'
print(a.islower())

a = 'This is just a TEST'
print(a.isupper())
a = 'THIS IS JUST A TEST'
print(a.isupper())

# https://docs.python.org/3/library/stdtypes.html