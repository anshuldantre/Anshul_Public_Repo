for x in range(151):
    print(x)

for x in range(0,1000,5):
    print(x)

divide_by_five = 1
divide_by_ten = 1
for x in range(1,101):
    divide_by_five = x / 5
    divide_by_ten = x / 10
    if divide_by_ten == int(divide_by_ten) :
        print('Coding Dojo')
    elif divide_by_five == int(divide_by_five):
        print('Coding')
    else:
        print(x)

val = 0
for x in range(500001):
    val = val + x
print(val)

x=500000
val = 0
while x > 0:
    val = val + x
    x -= 1
print(val)

for x in range(2018,0,-4):
    print(x) 


lownum = 3
highnum = 39
mult = 6
divide_by_mult = 1
for x in range(lownum,highnum):
    divide_by_mult = x/mult
    if divide_by_mult == int(divide_by_mult):
        print(x)
