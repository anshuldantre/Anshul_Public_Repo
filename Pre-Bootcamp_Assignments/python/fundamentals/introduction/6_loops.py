# range( START, STOP (optional), STEP (optional) )
# START: Inclusive of 1st
# STOP: Exclusive of 2nd
# STEP : Iterates by 3rd --INCREMENT/DECREMENT

for i in range (50):
    print(i)

for i in range (0,50):
    print(i)

for i in range (0,50,1):
    print(i)

for i in range (7,50,7):
    print(i)

# -------------------------------------------------------
for x in "Anshul":
    print(x)

# -------------------------------------------------------
my_list = [123,'xyz',456]
for i in my_list:
    print(i)

my_list = [123,'xyz',456]
for i in range(0,len(my_list)):
    print(i, my_list[i])

# -------------------------------------------------------
count = 0
while count < 5:
    print('Hello World')
    count +=1

# -------------------------------------------------------
count = 10
while count < 5:
    print('Hello World')
    count +=1
else:
    print("Count value too high")

# -------------------------------------------------------
for val in "string":
    print(val)
    if val == 'i':
        break

# -------------------------------------------------------
for val in "string":
    if val == 'i':
        continue
    print(val)

# -------------------------------------------------------
if 10 > 15:
    pass