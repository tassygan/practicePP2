from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]

print("map:", list(map(lambda x: x * 2, numbers)))
print("filter:", list(filter(lambda x: x % 2 == 0, numbers)))
print("reduce sum:", reduce(lambda a, b: a + b, numbers))