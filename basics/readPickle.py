import pickle

with open('students.pkl','rb') as f:
  students = pickle.load(f)

print(students)
