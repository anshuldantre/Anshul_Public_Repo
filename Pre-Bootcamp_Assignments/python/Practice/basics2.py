print(F'This is a way to the string with details')
a='GOOD'
b='Display'
c='Stuff'
print(F'This is a {a} way to {b} the string with {c} details')
print('This is another {} way to {} details and {}'.format(a,b,c))


a="Anshul"
b="DANTRE"
print(F'My name is {a} {b}')
print (a.upper())
print (b.lower())
print(a.split('n'))
print(a.count('s'))


a="Shradha"
b="Tripathi"
print("Any my wife's name is {} {}".format(a,b))


a="New"
b="old"
print(f'This is {a} way of display, forget the {b} way')
print('This is the {} way of display, forget the {} methods'.format(a,b))

a="Concatenate"
b="string"
print('This is how you '+a+' a '+b)
print('this is how you',a,'a',b)




# list
a = []
print(a)
b=[1,2,3,4,5]
print(b)
c=['abc','def','ghi','jkl']
print(c)
d=[123,'abc',456,'def',0.789,['GHI','JKL',[345,456,789]]]
print(d)
# print(d[5])
# print(d[5][1][2])
# print(d[5][2][0])
print(len(d))
e=[1,2,3,4,5,2.5,5.6,7.8,2.3,3.4,98,6.5,41.5]
print(max(e))
print(min(e))
print(sum(e))
print(sum(e)/len(e))
print(sorted(e))

f=["A","B","C","D"]
print(max(f))
print(min(f))
g=[1,2,3]
g.pop()
print(g)
g.append(4)
print(g)
g.insert(1,5)
print(g)
g.pop(0)
print(g)
print(type(g))

a=[1,2,3]
b=[4,5,6]
# c=a+b
# print(c)
c=a*5
print(c)
a[2]=a[0]
print(a)

a=[0,0,0,0,0,0,0,0,0,1,2,3,4,5,6,7,8,9,0]
print(a[1:5])
print(a[:3])
print(a[:])
print(a[5:])
print(a.index(7))

a=[4,3,2,1]
a.reverse()
print(a)



# tuples
a=('a','b','c','d',123,(9,8,7))
print(a)
print(type(a))
print(len(a))
print(a[2])
print(a[5][1])

# dictionary
import pprint
a = {"category 1": "1,1,1,1,1","Category 2":"2,2,2,2,2,2", "Category 3":"3,3,3,3,3,3,3,3,3,3,3,3,3,3,3"}
# print(a)
pprint.pprint(a)