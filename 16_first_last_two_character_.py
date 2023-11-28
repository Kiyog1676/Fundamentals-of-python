user=input("enter your string :")

if len(user)<2:
    first_two_char=user[:2]
    last_two_char=user[-2:]

    result=first_two_char and last_two_char(user)
    print("result :", result)





