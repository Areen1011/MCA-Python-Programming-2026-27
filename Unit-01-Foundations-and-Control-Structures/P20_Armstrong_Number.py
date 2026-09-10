num = int(input("Enter the number: "))
digits = len(str(num))
temp = num
sum = 0

while num > 0:
    digit = num % 10
    sum += digit ** digits
    num = num // 10

if sum == temp:
    print("It is an Armstrong number")
else:
    print("It is not an Armstrong number")