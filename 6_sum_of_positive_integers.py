n = int(input("Enter a number to calculate the sum of positive integers: "))
sum_positive = 0

for i in range(1, n + 1):
    print(i)
    if i > 0:
        sum_positive += i

print("Sum of positive integers =", sum_positive)