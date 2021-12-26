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
print('Your average is: ', total/len(grades))
print('Your high score is: ', max(grades))
print('Your low score is: ', min(grades))

for i in range (0, numGrades-1,1):
  for i in range (0, numGrades-1,1):
    if grades[i]<grades[i+1]:
      temp = grades[i]
      grades[i]=grades[i+1]
      grades[i+1]=temp


for grade in grades:
  print(grade)
  

