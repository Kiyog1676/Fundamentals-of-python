l1=["python","java","php","android"]

max=len(l1[0])

print(max)
word=""

for i in l1:
    if len(i)>max:
        word=i
        max=len(i)

print("max = ",max)
print("word =",word)