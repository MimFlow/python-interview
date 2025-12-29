"""What does “hashable” mean in Python"""


class MutablePoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)


# 1. Create and store
p = MutablePoint(1, 1)
my_dict = {p: 'Found it!'}

# 2. Mutate the object
p.x = 99

# 3. Try to retrieve
print(p in my_dict)  # Output: False (The object is "lost")
print(my_dict[p])  # Raises KeyError
