N = str(input("Enter a number: ")).strip()
sum = 0
for i in N:
    sum += int(i)
print("Sum of digits in integer N = " + str(sum))