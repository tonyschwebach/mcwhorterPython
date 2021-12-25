numGrades = int(input('How many grades would you like to enter? '))
grades=[]

while (len(grades) < numGrades):
  grades.append(int(input('Enter grade: ')))


def sortGrades(gradesArray):
  for j in range (0,len(gradesArray)-1,1):
    if gradesArray[j]<gradesArray[j+1]:
      temp = gradesArray[j]
      gradesArray[j]=gradesArray[j+1]
      gradesArray[j+1]=temp


sortGrades(grades)
print(grades)