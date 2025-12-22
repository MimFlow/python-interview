"""What is a closure in Python?"""


def outer(n):
    def inner(x):
        return x + n

    return inner


add_10 = outer(10)

print(add_10(10))
print(add_10(50))
