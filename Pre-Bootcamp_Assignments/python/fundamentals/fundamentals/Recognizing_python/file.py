num1 = 42   #- variable declaration, - Data Types - Primitive - Numbers

num2 = 2.3  #- variable declaration, - Data Types - Primitive - Numbers (A float type)

boolean = True  #- variable declaration, - Data Types - Primitive - Boolean

string = 'Hello World'  #- variable declaration, - Data Types - Primitive - Strings

pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # - variable declaration, -Composite - List - initialize

person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # - variable declaration, -Composite - Dictionary - initialize

fruit = ('blueberry', 'strawberry', 'banana') # - variable declaration, -Composite - Tuples - initialize

print(type(fruit)) #- type check,-Print

print(pizza_toppings[1])  #- Composite - List - access value,-Print

pizza_toppings.append('Mushrooms') #- Composite - List - add value

print(person['name']) #- Composite - Dictionary - access value,-Print

person['name'] = 'George' #- Composite - Dictionary - change value

person['eye_color'] = 'blue' #- Composite - Dictionary - add value

print(fruit[2]) #- Composite - Tuples- access value,-Print

if num1 > 45:                       #- conditional- if
    print("It's greater")           #- Print
else:                               #- conditional- else
    print("It's lower")             #- Print


if len(string) < 5:                 #- conditional- if, - length check
    print("It's a short word!")     #- Print
elif len(string) > 15:              #- conditional- else if, - length check
    print("It's a long word!")      # -Print
else:                               #- conditional- else
    print("Just right!")            # -Print


for x in range(5):                  #- for loop- start
    print(x)                        # -Print
for x in range(2,5):                #- for loop- start- stop
    print(x)                        # -Print
for x in range(2,10,3):             #- for loop- start- stop- increment
    print(x)                        # -Print


x = 0                               #- variable declaration- Data Types- Numbers
while(x < 5):                       #- while loop- start- stop
    print(x)                        # -Print
    x += 1                          #- while loop- increment


pizza_toppings.pop()                #- Data Types- Composite- List- delete value
pizza_toppings.pop(1)               #- Data Types- Composite- List- delete value

print(person)                       #- Data Types- Composite- Dictionary- access value,-Print
person.pop('eye_color')             #- Data Types- Composite- Dictionary- delete value
print(person)                       #- Data Types- Composite- Dictionary- access value,-Print

for topping in pizza_toppings:      #- for loop- start- stop- increment
    if topping == 'Pepperoni':      #- conditional- if
        continue                    #- for loop- continue
    print('After 1st if statement') # -Print
    if topping == 'Olives':         #- conditional- if
        break                       #- for loop- break

def print_hello_ten_times():        #- function
    for num in range(10):           #- for loop- start- stop- increment
        print('Hello')              # -Print

print_hello_ten_times()             #- function (call)

def print_hello_x_times(x):         #- function- parameter
    for num in range(x):            #- for loop- start- stop- increment
        print('Hello')              # -Print

print_hello_x_times(4)              #- function call- argument

def print_hello_x_or_ten_times(x = 10): #- function- argument,- variable declaration
    for num in range(x):                #- for loop- start- stop- increment
        print('Hello')                  #,-Print

print_hello_x_or_ten_times()            #- function
print_hello_x_or_ten_times(4)           #- function- argument


"""
Bonus section
"""

# print(num3)                       - NameError: name <variable name> is not defined
# num3 = 72                         - variable declaration, - Data Types - Primitive - Numbers
# fruit[0] = 'cranberry'            - TypeError: 'tuple' object does not support item assignment
# print(person['favorite_team'])    - KeyError: 'favorite_team'
# print(pizza_toppings[7])          - IndexError: list index out of range
#   print(boolean)                  - IndentationError: unexpected indent
# fruit.append('raspberry')         - AttributeError: 'tuple' object has no attribute 'append'
# fruit.pop(1)                      - AttributeError: 'tuple' object has no attribute 'pop'