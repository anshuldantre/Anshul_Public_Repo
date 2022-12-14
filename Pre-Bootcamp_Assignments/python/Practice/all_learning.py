#demonstrate a pass usage
a=35
if a<50:
    pass
else:
    print('else block')

# Primitive data types
# int
a=50
print(type(a))
# float
b=65.6565
print(type(b))
# sting
c='This is my string'
print(type(c))

# Composite data types
# list
a=[1,2,3,'a','b','c']
print(type(a))
# Tuples
b=(1,2,3,'a','b','c','d')
print(type(b))
# Dictionaries
c={"Car1":"Toyota","Car2":"Honda"}
print(type(c))


# Common functions
a=[1,2,3,'a','b','c']
b=(1,2,3,'a','b','c','d')
c={"Car1":"Toyota","Car2":"Honda"}
print(f"list length {len(a)}, tuple lenght {len(b)}, dictionary length {len(c)}")
