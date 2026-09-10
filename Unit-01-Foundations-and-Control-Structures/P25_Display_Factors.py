num = int(input("Enter the number: "))

count = 0

print("The factors of", num, "are:")

for i in range(1, num + 1):
    if num % i == 0:
        print(i)
        count += 1

print("The total number of factors is:", count)

