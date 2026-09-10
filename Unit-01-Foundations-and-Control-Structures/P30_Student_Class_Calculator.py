total, highest, lowest, pass_count, fail_count, above_75_count = 0, 0, 100, 0, 0, 0

n = int(input("Enter the number of students: "))

print("Enter marks of students: ")

for i in range(n):
    marks = int(input(f"Student {i + 1}: "))
    
    total += marks
    
    if marks > highest:
            highest = marks
    elif marks < lowest:
        lowest = marks
    
    if marks <= 35:
        fail_count += 1
    else:
        pass_count += 1
        
    if marks >= 75:
        above_75_count += 1


avg = total / n

print("Average marks of students:", avg)
print("Highest marks:", highest)
print("Lowest marks:", lowest)
print("Number of students who passed:", pass_count)
print("Number of students who failed:", fail_count)
print("Number of students with marks above 75:", above_75_count)