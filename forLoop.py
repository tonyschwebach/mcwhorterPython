# prompt user for number of grades
numGrades = int(input('How many grades would you like to enter? '))
grades = []
total = 0
# then ask for each grade
for i in range(0,numGrades,1):
  grade = float(input('What was your grade? '))
  grades.append(grade)
  total += grade
# then print each grade
print('Your average is: '+ str(total/len(grades)))
for grade in grades:
  print(grade)

