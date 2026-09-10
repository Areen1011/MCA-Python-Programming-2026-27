start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

count = 0

for num in range(start, end + 1):

    if num > 1:
        prime = True

        for i in range(2, num):
            if num % i == 0:
                prime = False
                break

    if prime:
        print(num)
        count = count + 1
        
print("Total number of prime numbers:", count)