num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

if num1 <= num2 and num1 <= num3:
    print("The smallest number is:", num1)
elif num2 <= num1 and num2 <= num3:
    print("The smallest number is:", num2)
else:
    print("The smallest number is:", num3)
    
if num1 >= num2 and num1 >= num3:
    print("The largest number is:", num1)
elif num2 >= num1 and num2 >= num3:
    print("The largest number is:", num2)
else:
    print("The largest number is:", num3)
    
# smallest = min(num1, num2, num3)
# largest = max(num1, num2, num3)

# print("The smallest number is:", smallest)
# print("The largest number is:", largest)

