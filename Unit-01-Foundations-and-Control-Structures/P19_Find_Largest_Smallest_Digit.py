num = int(input("Enter the number: "))

largest = 0
smallest = 9
count = 0

while num > 0:
    
    digit = num % 10
    count += 1
    
    if digit > largest:
        largest = digit
    
    if digit < smallest:
        smallest = digit
        
    num = num // 10

print("The number of digits is:", count)
print("The largest digit is:", largest)
print("The smallest digit is:", smallest)