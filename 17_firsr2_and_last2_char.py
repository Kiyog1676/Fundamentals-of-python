string=input("enter your string:")

if len(string)<2:
    print("empty string :")
else:
    s2=string[:2]+string[-2:]
    print(s2)
