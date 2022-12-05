count = 0
while (count < 5):
    print('Looping - ',count)
    count += 1

y = 3
while (y > 0):
    print(y)
    y = y-1
else:
    print('Final else statement')


y = 3
while (y > 5):
    print(y)
    y = y-1
else:
    
    print('Final else statement')

y = 3
while (y > 0):
    print(y)
    y=y-1
    if y == 0:
        break
else:
    print('Final else statement')