def countdown(x):
    a=[]
    while x > 0:
        a.append(x)
        x = x-1
    else:
        a.append(x)
    return a

count_list = countdown(16)
print(count_list)


def countdown(x):
    a=[]
    for i in range(x,-1,-1):
        a.append(i)
    return a

count_list = countdown(8)
print(count_list)

"""-------------------------------------"""

def print_and_return (a,b):
    print('This is print',a)
    return b

x=print_and_return(1,2)
print('this is return',x)

"""-------------------------------------"""

def first_plus_length(my_list):
    return(my_list[0] + len(my_list))

a=[5,6,7,8,9,10,12,13,14,15,16,17]
b=first_plus_length(a)
print(b)

"""-------------------------------------"""

def value_greater_than_second(my_list):
    if len(my_list) < 2:
        return False

    a=[]
    num=my_list[1]
    for x in range(0,len(my_list)):
        if my_list[x] > num:
            a.append(my_list[x])
    
    print(len(a))
    return a
    
p=[1,2,3,4,5,6,7,8,9,1,1,1,1]
q=[99]
r=value_greater_than_second(p)
print(r)
s=value_greater_than_second(q)
print(s)

"""-------------------------------------"""

def length_and_value(size,value):
    y=[]
    for x in range(0,size):
        y.append(value)

    return y

a=length_and_value(4,7)
b=length_and_value(6,2)
print(a)
print(b)

"""-------------------------------------"""