#1
def squares(n):
    for i in range(n + 1):
        yield i * i

N = int(input("N: "))
for x in squares(N):
    print(x)

#2
def evens(n):
    for i in range(0, n + 1):
        if i % 2 == 0:
            yield i

n = int(input("n: "))
print(",".join(str(x) for x in evens(n)))

#3
def div(n):
    for i in range(0, n + 1):
        if i%3==0 and i%4== 0:
            yield i

n = int(input("n: "))
for x in div(n):
    print(x)

#4
def squares(a, b):
    for i in range(a, b + 1):
        yield i * i

a = int(input("a: "))
b = int(input("b: "))

for val in squares(a, b):
    print(val)

#5
def down(n):
    for i in range(n, -1, -1):
        yield i

n = int(input("n: "))
for x in down(n):
    print(x)
