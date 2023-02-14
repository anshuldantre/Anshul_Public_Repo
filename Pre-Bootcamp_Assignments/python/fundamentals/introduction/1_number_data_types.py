# Int & float dataypes
x = 10
y = 22.5

print(x+y)
print (f'The dataype is {type(x+y)} and after int converting datatype is {type(x + int(y))} and after float conversion datatype is {type(float(x)+y)}')

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Random Number generator between a set of given values
import random
print(random.randint(1,5))
print(random.randint(-100,5))

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Random float between 0.0 & 1.0
import random
print(random.random())

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Random choice between a set of given values
import random
print(random.choice(['A','B','C','D','E','F','G','H','I','J','K','L']))