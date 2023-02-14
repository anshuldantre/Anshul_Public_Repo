# Functions can be defined and called anywhere in the file. If its in another file, we can impirt that file and use the function from that file
# define function_name (parameter) ==> def calculate (param1, param2)
# When we call paramter becomes arguments
# Function not always return a value but can alter the program. FO functions returning a value we need a variable to hold that value
# Whatever we return from Function variable becomes that, like function returning string becomes a string, function returning list becomes a list

def add(a,b):
    x=a+b
    return x

new_val = add(5,6)
print(new_val)
print(add(2,3))

# -------------------------
def say_hi(name):
    print ("Hi "+name)

say_hi("Michael")
say_hi("Anna")
say_hi("Eli")

# -------------------------
def say_hi(name):
    return "Hi " + name
greeting = say_hi("Michael")    # the returned value from say_hi function gets assigned to the 'greeting' variable
print(greeting)                 # this will output 'Hi Michael'

# -------------------------
def add(a, b):
    x = a + b
    return x
sum1 = add(4,6)
sum2 = add(1,4)
sum3 = sum1 + sum2

# Return Also Means Exit & Print Statements are for Debugging
# Many students at first have trouble understanding the difference between a print statement and a return statement. There are two big differences:

# Saving values: When you print something with  print(), strictly speaking, it doesn't have any affect on your program. No data is saved or changed or passed anywhere else in the program. 
# Print statements are primarily used for programmers to debug the code, to see what's happening in the program. On the other hand, a return statement may pass a value back to the outer 
# scope after it's done running for the program to use!
# Exiting the function: Reaching a return statement always means "EXIT THIS FUNCTION NOW" whether or not there is more code. Any remaining code will not be run.

# -------------------------
# default parameters
def be_cheerful(name='Shradha', repeat=2): #his is the way to deault a parameter
    print(f'Good Morning {name} \n' * repeat)

be_cheerful('Anshul', 1)
be_cheerful()
# be_cheerful(4,"Benny Bob") # Breaks with error "can't multiply sequence by non-int of type 'str'"
be_cheerful(repeat=4,name="Benny Bob")

# ------------------
# Debugging with Print, Fix the code below by identifying the problem using print statements to debug the code
def multiply(num_list, num):
    for x in num_list:
        x *= num
    return num_list

a = [2,4,10,16]
b = multiply(a,5)
print(b)

# output:
# >>>[2,4,10,16]