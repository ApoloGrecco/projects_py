# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

# Write your code below this row 👇

sum_heights = 0
numbers_students = 0

for n in student_heights:
    sum_heights += n
    numbers_students += 1

medium_height = round(sum_heights / numbers_students)

print(medium_height)
