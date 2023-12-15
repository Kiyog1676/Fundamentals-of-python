n = int(input("Enter your number : "))
sum_positive = 0

for i in range(1, n + 1):
    print(i)
    if i > 0:
        sum_positive += i

print("Sum is =", sum_positive)