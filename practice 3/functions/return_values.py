#Functions can return values using the return statement:
def my_function(x, y):
  return x + y

result = my_function(5, 3)
print(result)

#Functions can return any data type, including lists, tuples, dictionaries, and more.
def my_function():
  return ["apple", "banana", "cherry"]

fruits = my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2])


#Positional-Only Arguments
def my_function(name, /):
  print("Hello", name)

my_function("Emil")

#Keyword-Only Arguments
def my_function(*, name):
  print("Hello", name)

my_function(name = "Emil")

#Combining Positional-Only and Keyword-Only
def my_function(a, b, /, *, c, d):
  return a + b + c + d

result = my_function(5, 10, c = 15, d = 20)
print(result)