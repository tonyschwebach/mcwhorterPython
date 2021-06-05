numGrades = int(input('How many grades would you like to enter? '))
grades=[]

while (len(grades) < numGrades):
  grades.append(int(input('Enter grade: ')))


def sortGrades(gradesArray):
  for i in range (0,len(grades)-1,1):
    for j in range (0,len(grades)-1,1):
      if grades[j]<grades[j+1]:
        temp = grades[j]
        grades[j]=grades[j+1]
        grades[j+1]=temp


sortGrades(grades)
print(grades)