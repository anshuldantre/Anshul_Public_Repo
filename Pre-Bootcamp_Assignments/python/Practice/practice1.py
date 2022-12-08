#data types
x=5
print(x)

y=True
print(y)

z='Anshul'
print(y)

a=2.456
print(a)


p=[7,8,9,10,11]
print(p)
print(p[3])
print(p[1:2])
print(p[2:])
print(p[:2])
print(p[:])
p.pop()
print(p)
p.pop(1)
print(p)
p.append(12)
print(p)
print(p.index(12))
p=[7,8,9,10,11]
print(len(p))
print(max(p))
print(min(p))


x=(4,5,6,7)
print(type(x))
print(x)

import pprint
x={"cat1":"val1,Val11,val111,val1111","cat2":"val2,Val22,val222,val2222","cat3":"val3,Val33,val333,val3333"}
print(type(x))
print(x)
pprint.pprint(x)

a="Anshul"
b=39
print(F'My name is {a} and my age is {b}')
print('Running on '+str(b)+', my name is '+a)
print('Hey there, My name is {} and my age is {}'.format(a,b))
print(a.split('s'))
print(a.lower())
print(a.upper())

import random
print(random.randint(2,2000))

a=['chevy','corolla','cayene']
b=['hayabusa','harley','hamilton']
c=a+b
d=b+a
print(c)
print(d)
print(sorted(c))
c.reverse()
print(c)



a=500
b=100
c=800
if a>b and a>c:
    print('A is Biiger')
elif b>a and b>c:
    print('B is Bigger')
else:
    print('C is bigger')


for x in range(3):
    print(x)

for x in range(3,5):
    print(x)

for x in range(5,8,2):
    print(x)

a=[5,6,7,8,9]
for x in range(len(a)):
    print(a[x])

a=[5,6,7,8,9]
for x in a:
    print(x)

for x in "Anshul":
    print(x)
