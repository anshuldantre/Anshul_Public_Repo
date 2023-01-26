# - create a function that, given an input string, returns a boolean whether parenteses in that string are valid. given input "y(3(p)p(3)r)s", returns true.
#     given "n(0(p)3", return false. given "n)0(t(0)k", return false


# x = 'y(3(p)p(3)r)s'
# x = 'n(0(p)3'
# x = 'n)0(t(0)k'
x = '((((((((((dkjfsdf))))))))))'
count_open = 0
count_close = 0
start_element = ''

for i in x:
    if (i == '('):
        if count_open == 0 and start_element == '':
            start_element = 'o'
        count_open += 1
    elif (i == ')'):
        if count_close == 0 and start_element == '':
            start_element = 'c'
        count_close += 1

# print(count_open)
# print(count_close)
# print(start_element)

if count_open == count_close and (count_open > 0 and count_close > 0) and start_element == 'o':
    print('Its equal')
elif count_open == count_close and (count_open == 0 and count_close == 0):
    print('Its equal but not paranthesis')
else:
    print ('Not equal')