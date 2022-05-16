#Write a program to check if a number is positive or not
'''
n = float(input("enter number:"))
if n > 0:
    print("positive number")
elif n==0:
    print(zero)
else:
    print("negative number")
'''
n = int(input("enter number:"))
a = n > 0
print("positive number",a)
b = n==0
print("negative number",b)
