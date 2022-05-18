#Write a Python Program to print max numbers in given 3 numbers ?
a = int(input("enter number:"))
b = int(input("enter number:"))
c = int(input("enter number:"))

largest = 0
if a < b and a < c:
    largest = a
elif b > c:
    largest = b
else:
    largest = c
    
print(largest,"maximum of three number")