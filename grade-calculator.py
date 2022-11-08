math_grade = int(input("Please enter your math score:  "))
biology_grade = int(input("Please enter your biology score:  "))
chemistry_grade = int(input("Please enter your chemistry score:  "))
sociology_grade = int(input("Please enter your sociology score:  "))
physics_grade = int(input("Please enter your physics score:  "))

# calculate the total grade
total_grade = math_grade + biology_grade + chemistry_grade + sociology_grade + physics_grade
count = 5
# print(f"the sum of all the grade is {total_grade}")
# calculate the average 
grade_point_average = total_grade / count

print(f"the average of all the grade is {grade_point_average}")
if grade_point_average > 90:
    print(f"You have A".format(grade_point_average))

if grade_point_average < 90 and grade_point_average > 80 :
    print(f"You have B".format(grade_point_average))

if grade_point_average < 80 and grade_point_average > 70 :
    print(f"You have C".format(grade_point_average))

if grade_point_average < 70 and grade_point_average > 60 :
    print(f"You have D".format(grade_point_average))

if grade_point_average < 60 :
    print(f"Sorry you have Failed ".format(grade_point_average))


