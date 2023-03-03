# - Write a function that accepts a list and returns whether that List has an even amount of values or an odd amount of values. oddOrEvenList([1,2,3]) should return odd while  oddOrEvenList([1,2,3,4]) will return even

    # - write a function that given a string date such as "12/07/2022", return whether or not that a person's birthday has passed this year. Birthday("07/29/1993") should return true
    # bonus - return a string with the users current age and whether or not they have had a birthday, Birthday("07/29/1993") should return "User is currently 29 years old and has had their birthday this year"



def even_odd(arr):
    a=len(arr)
    #print(a)
    if a%2 == 0:
        return 'Even number'
    else:
        return 'Odd Number'


a=[1,2,3,4,5]
b=even_odd(a)
print(b)



from datetime import date
today= date.today() 

def dob_pass(dob):
    month = int(dob[0:2])
    day   = int(dob[3:5])
    year  = int(dob[6:])
    #print(month)
    #print(day)
    #print(year)

    current_age = 2022 - year
    #print(current_age)
    print(today)

    # if today > dob:
    #     return(F'User is currently {current_age} years old and he/she has not had their birthday this year')
    # else:
    #     return(F'User is currently {current_age} years old and he/she has  had their birthday this year')

    return today


a='2022-12-05'
b=dob_pass(a)
print(b)




x = today- 

print(today)




#month <=12 and day <= 7: 


a="12/07/2022"
print(a[3:5])


# =-----------------------------------
str1  = "Anshul Dantre was here"
str2 = "was"
split_list=str1.split(str2)
concat_str = ""

for i in split_list:
    concat_str = concat_str + i

print(concat_str)


str1  = "Anshul 123 Dantr2386748248111111e was here 1"
# str1 = str1.islower()
str2 = "1"
new_str =""
for i in str1:
    if i != str2:
        new_str += i
print(new_str)