mathematics = int(input("Enter marks in Mathematics: "))
physics = int(input("Enter marks in Physics: "))
chemistry = int(input("Enter marks in Chemistry: "))

percentage = (mathematics + physics + chemistry) / 3

if mathematics >= 60 and physics >= 50 and chemistry >= 40:
    if percentage >= 60:
        print("The student is eligible for admission.")
    else:
        print("The student is not eligible for admission.")
else:
    print("The student is not eligible for admission.")