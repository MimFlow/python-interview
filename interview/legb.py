"""What's LEGB rule in Python"""

# Note: input is a built-in name, and using it as
# a variable name called shadowing

# G: Global scope
input = 'I am a Global Variable'


def outer_func():
    # E: Enclosing scope
    input = 'I am an Enclosing variable'  # noqa

    def inner_func():
        # L: Local scope
        input = 'I am a Local variable'
        print(input)

    inner_func()


outer_func()
# print(notfound)
