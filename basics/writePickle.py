import pickle

numStudents = int(input("How many students do you have? "))
students = {}

for x in range (0,numStudents,1):
  studentName = input("Student name: ")
  studentScore = int(input("Student score: "))
  students[studentName] = studentScore

with open('students.pkl','wb') as f:
  pickle.dump(students,f)
