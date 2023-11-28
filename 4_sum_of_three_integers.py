#  Write a Python program to sum of three given integers. However, if
# two values are equal sum will be zero

num1=int(input("enter number of first integers : "))
num2=int(input("entet number of second integers :"))
num3=int(input("enter number of third integers :"))


if num1==num2 or num2==num3 or num1==num3:
    print("sum is ",0)
else:
    print("sum is",num1+num2+num3)
    