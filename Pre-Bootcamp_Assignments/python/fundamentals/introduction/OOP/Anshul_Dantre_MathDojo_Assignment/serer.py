class MathDojo:
    def __init__(self):
        self.result = 0

    def add(self, arg1, *args):
        self.result = self.result + arg1
        for i in args:
            self.result += int(i)
        return self

    def substract(self, arg1, *args):
        self.result = self.result - arg1
        for j in args:
            self.result -= int(j)
        return self

md = MathDojo()
x = md.add(2).add(2,5,1).substract(3,2)
print(x.result)

# y = md.add(2)
# print(y.result)
# md.add(3,4)
# print(y.result)
# md.add(4,5,6)
# print(y.result)
# md.add(7,8,9)
# print(y.result)

# z = md.substract(1)
# print(z.result)
# md.substract(1,2)
# print(z.result)
# md.substract(1,2,3)
# print(z.result)
# md.substract(1,1,1,1,1,1,1,1,1,1,1,1)
# print(z.result)