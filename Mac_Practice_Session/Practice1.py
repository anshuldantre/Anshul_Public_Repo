# Users/anshuldantre/Desktop/DoJo/Pre-Bootcamp_Public/Pre-Bootcamp_Public/Mac_Practice_Session
# Pass statement, to be used when code is no compelte but we still want to progress
def my_func():
    print("Within function call")
    x = 5
    if x > 5:
        pass
    else:
        pass

my_func()

#---------------------------------------------------------------------------------------------------
# Primitive data types
# Integer
p = 57657
# String
q = 'Anshul Dantre'
# Float
r = 3.14
# Boolean
s = True
print(f"p = {p}\nq = {q}\nr = {r}\ns = {s}")

#---------------------------------------------------------------------------------------------------
# Tuples - A type of data that is immutable (can't be modified after its creation) and can hold a group of values. Tuples can contain mixed data types.
a = ("Anshul", "Dantre", 39, True)
print(a)

# Lists - A type of data that is mutable and can hold a group of values. Usually meant to store a collection of related data
b = ["Anshul", "Dantre", 39, True]
print(b)

# Dictionaries - A group of key-value pairs. Dictionary elements are indexed by unique keys which are used to access values. 
c = {"first_name":"Anshul", "last_name":"Dantre","age":39,"married":True}
print (c)

#---------------------------------------------------------------------------------------------------
# Common functions and syntax to invoke them function_name(variable name) --Remember function call always needs a brackets
# Type function to know the datatype of the input variable name. Input can be any data type int, float, boolean, tuple, list, dictionary
print(type(s))
# len function to know the lenght of the input variable. Not for integer, float of boolean, runs into an error when used with it. Gives the number of elements for tuples, list & dictionary & string length when used with string
print(len(a))
print(len(b))
print(len(c))
print(len(q))

#---------------------------------------------------------------------------------------------------
# Random number generator
import random
print(f"random {random.randint(4,96)}")
print(f"random {random.random()}")
print(f"random {random.uniform(3.2323,6.343443)}")

#---------------------------------------------------------------------------------------------------
# string concatenation and print statement variations
strng = "My name is"
full_name = 'Anshul Dantre'
print(strng + full_name)
print('The name is ' + full_name)

#An integer type cannot be concatenated to a string unless type casted
user_val = 100
# print('String doesnt gets concatenated to a integer variable ' + int_val)
print("String doesnt gets concatenated to a integer variable " + str(user_val))
print(f'values p={p}')
print(" Values are {}, {}, {} and {}".format(p,q,r,s))
print(q.title())

#---------------------------------------------------------------------------------------------------
# String functions to be invoked as string.function_name()
print(q.upper())
print(q.lower())
print(q.count('n'))
print(q.split(' '))
print(q.find('Dan'))
print('This'.isalnum()) #returns false if string has space
print("nsdknfds".isalpha())
print("1234".isdigit())
print(q.islower())
print(q.isupper())
print(q.endswith('e'))
print(q.join(b))