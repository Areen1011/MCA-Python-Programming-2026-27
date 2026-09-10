n = int(input("Enter the number of terms: "))

a, b = 0, 1
sum = 0

for i in range(n):
    print(a)
    sum += a
    a, b = b, a + b

print("The sum of the Fibonacci series is:", sum)