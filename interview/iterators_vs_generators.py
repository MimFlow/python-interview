"""Iterators vs. Generators"""

import time  # noqa: F401
from datetime import datetime


class Timer:
    def __iter__(self):
        return self

    def __next__(self):
        time.sleep(1)
        return time.time()


def timer_gen():
    while True:
        yield time.time()
        time.sleep(1)


timer = timer_gen()  # to be implemented

# Print time every second
for tick in timer:
    print(datetime.fromtimestamp(tick).strftime('%H:%M:%S'))
