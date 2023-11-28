str=input("enter your string :")

if "not poor" in str:
    str1=str.lower().replace("not poor","good")
    print(str1)
else:
    print(str)