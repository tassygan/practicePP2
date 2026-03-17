names = ["Ali", "Aruzhan", "Dana"]
scores = [90, 85, 95]

for i, name in enumerate(names):
    print(i, name)

for name, score in zip(names, scores):
    print(name, score)

value = "100"
print(value, type(value))
value = int(value)
print(value, type(value))