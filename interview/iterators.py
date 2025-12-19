"""Iterators in Python"""


class CounterIterator:
    def __init__(self, n):
        self.n = n

    def __next__(self):
        if self.n <= 0:
            raise StopIteration

        self.n -= 1
        return self.n


class Counter:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return CounterIterator(self.n)


counter = Counter(10)

print(list(counter))
print(list(counter))
print(list(counter))
print(list(counter))

c = Counter(10)

print(list(c))

i = iter(c)

print(i, type(i))
