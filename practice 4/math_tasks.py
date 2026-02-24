#1 task
import math 
d=int(input("Input degree: "))
rad=d* math.pi /180
print ("Output radian:", rad )

#2 task
h= int(input("Heigh: "))
val1=int(input("Base, first value: "))
val2=int(input("Base, second value: "))
area=((val1+val2)/2)*h
print ("Expected Output:", area)

#3 task
n= int(input("Input number of sides: "))
s= float(input("Input the length of a side: "))

area = (n*s*s) / (4 * math.tan(math.pi/ n))
print("The area of the polygon is:", area)

#4 task
base= float(input("Length of base: "))
height= float(input("Height of parallelogram: "))

a=base*height
print("Expected Output:", a)