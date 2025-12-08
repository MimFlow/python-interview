"""
is vs. equality (==) in python?
"""

a = [1, 2, 3]
b = [1, 2, 3]
c = b

print(a == b)
print(a is b)
print(b is c)

print(id(a))
print(id(b))
print(id(c))

if status is None:
    ...

if user.age == 18:
    ...


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)


p1 = Point(1, 2)
p2 = Point(1, 2)

print(p1 == p2)  # True
print(p1 is p2)  # False
