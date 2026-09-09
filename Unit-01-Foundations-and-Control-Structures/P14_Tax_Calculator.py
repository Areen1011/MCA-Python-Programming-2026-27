income = int(input("Enter annual income: "))

if income <= 1200000:
    tax = 0
elif income <= 1600000:
    tax = (income - 1200000) * 0.15
elif income <= 2000000:
    tax = (income - 1600000) * 0.20
else:
    tax = (income - 2000000) * 0.25

print("Tax payable =", tax)