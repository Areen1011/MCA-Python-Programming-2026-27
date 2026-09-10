a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

x = a
y = b

while b != 0:
    a, b = b, a % b
    
gcd = a
lcm = (x * y) // gcd

print("The GCD of", x, "and", y, "is:", gcd)
print("The LCM of", x, "and", y, "is:", lcm)