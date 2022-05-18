#Write a Python Program to print min numbers in given 3 numbers ?
a = int(input("enter number:"))
b = int(input("enter number:"))
c = int(input("enter number:"))
smallest = 0

if a < b and a < c:
    smallest = a
elif b < c:
    smallest = b
else:
    smallest = c
    
print(smallest,"minimum of three number")

'''
x = {'a':5,'b':10}
y = dict(zip(x.values(),xkeys()))
print(y)
'''