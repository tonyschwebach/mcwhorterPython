numGrades = int(input('How many grades would you like to enter? '))
grades=[]

i = 1
while (i<=numGrades):
  grades.append(int(input('What was your score? ')))
  i+=1

j=0
while (j<numGrades):
  print(grades[j])
  j+=1