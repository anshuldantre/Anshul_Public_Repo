a = [1,2,3,'a','b','c']
print(a)
print(len(a))
print(a[:])
print(a[:2])
print(a[4:])
print(a[1:3])

b=['a','b','c',1,2,3]
print(b)

c=a+b
print(c)
print(type(c))


s=('x','y','z',10,9,8)
print(s)
print(type(s))

p={"key1":"val1","key2":"val2","key3":"val3"}
print(p)
print(type(p))

for key, val in p.items():
    print(F"Key =  {key} and value = {val}")

a= {"key1":[1,2,3],"key2":[4,5,6],"key3":[7,8,9]}
print(a)
# print(type(a))
print(a["key2"][2])
