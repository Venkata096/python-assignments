#Write a Python Program to print the greatest number in given three numbers?
a = int(input("enter first number:"))
b = int(input("enter second number:"))
c = int(input("enter third number:"))
if a > b and a > c:
    largest = a
elif b > c:
    largest = b
else:
    largest = c
    print(largest,"is the largest of the number")