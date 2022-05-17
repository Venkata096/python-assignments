#Write a Python Program to print given 3 numbers in descending order?
a = int(input("enter number:"))
b = int(input("enter number:"))
c = int(input("enter number:"))
if a < b:
    a,b = a,a
if b < c:
    a,c = c,a
if b < c:
    b,c = c,b
print(a, ">",b,">",c)