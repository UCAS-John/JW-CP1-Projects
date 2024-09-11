# John Wangwang Average Grade

default_value = 0
Grade = [default_value] * 6
AvgGrade = float(0)

for i in range(0, 6):
    Grade[i] = float(input(f"Type your {i+1} Class Grade: "))
    
for grade in Grade:
    AvgGrade += grade

AvgGrade /= 6

print(f"Your Average grade is {AvgGrade} ")