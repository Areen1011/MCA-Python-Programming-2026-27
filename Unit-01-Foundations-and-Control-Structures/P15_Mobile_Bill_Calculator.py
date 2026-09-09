data = int(input("Enter the data consumption (in GB): "))

if data <= 2:
    bill_amount = data * 10
elif data <= 5:
    bill_amount = data * 15
else:
    bill_amount = data * 20