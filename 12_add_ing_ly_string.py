string=input("enter your string :")

if len(string)>=3:
   if string.endswith("ing"):
    new_string=string+"ly"
    print("after adding ly :",new_string)

   else:
    new_string=string+"ing"
    print("after adding ing :",new_string)

else:
  print("string unchanged")