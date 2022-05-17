#Write a Python Program to print given 3 numbers in ascending order?
a = int(input("enter number:"))
b = int(input("enter number:"))
c = int(input("enter number:"))
if a > b:
    a,b = b,a
if a > c:
    a,c = c,a
if b > c:
    b,c = c,b
    
print(a, "<",b,"<",c)
'''
a = [10,30,80,55,90,67,88,33,23,1,5,6,7]
print(sorted(a))
'''