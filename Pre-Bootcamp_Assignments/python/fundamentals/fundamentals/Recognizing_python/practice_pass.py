x = 10
if x > 50:
    print('Bigger than  50')
else:
    print('lesser than 50')
    if x > 5:
        pass
        print(type(x))
        #print('Bigger than 5')
    else:
        print('smaller than 5')

am_i_hungry = True
want_to_eat_again = False
print(am_i_hungry)
print(want_to_eat_again)

age = 39
weight = 165.56
print(age)
print(weight)

name = 'Anshul Dantre, aspiring to be a coding Ninja'
print(name)


dog = ('Bruce', 'cocker spaniel', 19, False)
print(dog[1])
dog[1] = 'dachshund'


empty_list = []
ninjas = ['Rozen', 'KB', 'Oliver']
print(ninjas[2])
ninjas[0]='Francis'
ninjas.append('Michael')
print(ninjas)
ninjas.pop()
print(ninjas)
ninjas.pop(1)
print(ninjas)
ninjas.append(123.123)
print(ninjas)


empty_dict = {}
new_person = {'name':'Anshul', 'age':39, 'weight':165.2,'has_glasses':False}
new_person['name'] = 'Rahul'
new_person['hobbies'] = ['climbing','coding']
print(new_person)
w=new_person.pop('weight')
print(w)
print(new_person)
print(type(new_person))
print(type(w))
print(len(new_person))
print(len(empty_dict))


print(type(24))
print(type(3.9))
print(type(3j))


int_to_float=25
print(type(int_to_float))
int_to_float = float(int_to_float)
print(int_to_float)
print(type(int_to_float))

float_to_int = 35.99
print(type(float_to_int))
float_to_int = int(float_to_int)
print(float_to_int)
print(type(float_to_int))

int_to_complex = 35
print(type(int_to_complex))
int_to_complex = complex(int_to_complex)
print(int_to_complex)
print(type(int_to_complex))

import random
print(random.randint(2,5))