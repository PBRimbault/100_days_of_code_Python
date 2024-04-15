# def add(*args):
#     total = 0
#     for n in args:
#         total += n
#     return total

# print(add(1, 25, 84, 19))

def calculate(n, **kwargs):
    print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    return n


print(calculate(2, add=3, multiply=5))