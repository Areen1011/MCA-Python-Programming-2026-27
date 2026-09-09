units = float(input("Enter the number of units consumed: "))

if units <= 100:
    bill_amount = units * 5
elif units <= 200:
    bill_amount = units * 7
else:
    bill_amount = units * 9 

print("The electricity bill amount is: ", bill_amount)