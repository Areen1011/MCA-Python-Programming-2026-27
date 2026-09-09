age = int(input("Enter age: "))
income = int(input("Enter income: "))
credit = int(input("Enter credit score: "))

if age >= 18 and income >= 30000 and credit >= 650:
    print("Eligible for loan")
else:
    print("Not eligible for loan")