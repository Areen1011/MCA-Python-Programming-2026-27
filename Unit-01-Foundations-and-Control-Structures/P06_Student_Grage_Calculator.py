percentage = int(input("Enter the percentage obtained: "))

if percentage < 0 or percentage > 100:
    print("Invalid percentage. Please enter a value between 0 and 100.")
elif percentage >= 90:
    print("A Grade")
elif percentage >= 80:
    print("B Grade")
elif percentage >= 70:
    print("C Grade")
elif percentage >= 60:
    print("D Grade")
else:
    print("F Grade")