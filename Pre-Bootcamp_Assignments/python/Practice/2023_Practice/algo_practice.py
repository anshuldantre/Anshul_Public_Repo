# create a function that returns whether the secondstring is a permutation of the first. For example, given ("mister", "stimer"), return true. given ("mister", "sister"), return false

def is_permutation(str1, str2):
    if len(str1) != len(str2):
        return False
    
    my_dict_str1 = {}
    my_dict_str2 = {}

    for i in range(len(str1)):
        if str1[i] not in my_dict_str1:
            my_dict_str1[str1[i]] = 1
        else:
            my_dict_str1[str1[i]] += 1
        if str2[i] not in my_dict_str2:
            my_dict_str2[str2[i]] = 1
        else:
            my_dict_str2[str2[i]] += 1
    return my_dict_str1 == my_dict_str2

print(is_permutation("mister", "sister"))
print(is_permutation("mister", "stimer"))
print(is_permutation("mister", "itimer"))

# ------------------------------------------------------------------------------
from collections import Counter
def is_permutation(one, two):
    return Counter (one) == Counter (two)

print(is_permutation("mister", "sister"))
print(is_permutation("mister", "stimer"))
print(is_permutation("mister", "itimer"))

# ------------------------------------------------------------------------------
def is_permutation(value1, value2):
    if len(value1) == len(value2):
        new1=sorted(value1)
        new2=sorted(value2)
        if new1 == new2:
            return True
        else:
            return False
    else:
        return False

print(is_permutation('mister', 'stimer'))
print(is_permutation("mister", "sister"))
print(is_permutation("mister", "itimer"))