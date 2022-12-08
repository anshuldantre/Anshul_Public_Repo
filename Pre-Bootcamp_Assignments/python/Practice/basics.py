print('Hello World!')
print("Hello World!")
print("Hello" + 'World!')
print("Hello", 'World!')

fav_car1="Lamborghni"
fav_car2="Ferrari"
print(f' {fav_car1} and {fav_car2} are my most favourite cars')

i = 10
f = 2.3456789
c = "This is a string"
print(i)
print(f)
print(c)

f = int(f)
print(f)
i = float(i)
print(i)
i = c
print(i)

name = ['Anshul', 'Bhushan', 'Charu', 'Daru', 'Erick', 'Fontelli']
print(name[3])
name.pop(2)
print(name)
name.pop()
print(name)
name.append('Gagan')
print(name)
name.insert(1,'harish')
print(name)

name = ['Anshul', 'Bhushan', 'Charu', 'Daru', 'Erick', 'Fontelli']
print(max(name))
print(min(name))
print(len(name))
print(name[-2])
print(name[2:5])
print(name[:2])
print(name[4:])
print(name[-4:])
print(name[-1:-4])
if 'Charu' in name:
    print('Charu found in the list')
else:
    print('NOT found in the list')
name[0]="Shrimp"
print(name)