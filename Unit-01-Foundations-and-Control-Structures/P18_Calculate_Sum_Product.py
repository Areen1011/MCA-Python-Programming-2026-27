num = int(input("Enter the number: "))

sum = 0
product = 1

while num > 0:
    digit = num % 10
    sum += digit
    product *= digit
    num = num // 10

print("The sum of digits is:", sum)
print("The product of digits is:", product)
