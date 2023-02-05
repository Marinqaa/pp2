# 1
class with2meth:
    def getString(self):
        self.s = input()
    def printString(self):
        print(self.s.upper())

UserInput = with2meth()
UserInput.getString()
UserInput.printString()

# 2
class Shape:
    def __init__(self):
        pass
    def area(self):
        return 0
class Square(Shape):
    def __init__(self, l):
        self.length = l
    def area(self):
        a = self.length * self.length
        return a
s = Square(int(input()))
print(s.area())
