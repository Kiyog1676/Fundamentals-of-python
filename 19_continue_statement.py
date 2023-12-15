"""
continue statement: it will skip the correct statement but loop will continue.

"""

for i in range(1,6):
    marks=int(input("enter your marks :"))
    if marks<=35:
        print("pass")
        continue
    else:
        print("fail")


