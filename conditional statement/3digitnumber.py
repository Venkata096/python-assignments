# Write a Python Program to check if a number is a 3-digit number or not?
'''
n = int(input("enter your number:"))
if (n <500 and  n> 99):
    print("{} is a 3 digit number".format(n))
else:
    print("{} is a not 3 digit number".format(n))
'''   
n = int(input("enter number:"))
if n < 500 and n > 99:
    print("is a 3 digit number".format(n))
else:
    print("is a not 3 digit number".format(n))