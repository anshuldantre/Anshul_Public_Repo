# Tuples are just like list but are immutable (We cant change them)
# Indexed starting at 0 # Have built in methods # Defined within parathensis # can store any data we want to store, just length is fixed

my_first_tuple = ()
print(f'My first tuple is {my_first_tuple}')

my_first_tuple = (1,2,3,4,5)
print(f'My first tuple is {my_first_tuple}')

my_first_tuple = ('A','B','C','D','E')
print(f'My first tuple is {my_first_tuple}')

my_first_tuple = (1,'A',2,'b',3,'C',4,'d',5,'E')
print(f'My first tuple is {my_first_tuple}')

my_first_tuple_within_tuple = (1,('A','x','Y','z'),2,'b',(3,7,8,9),'C',4,'d',5,'E')
print(f'My first tuple is {my_first_tuple_within_tuple}')

my_first_list_within_tuple = (1,['A','x','Y','z'],2,'b',(3,7,8,9),'C',4,'d',5,'E')
print(f'My first tuple is {my_first_list_within_tuple}')

my_first_tuple_within_list = [1,('A','x','Y','z'),2,'b',(3,7,8,9),'C',4,'d',5,'E']
print(f'My first tuple is {my_first_tuple_within_list}')

