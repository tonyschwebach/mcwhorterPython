from typing import Match


class Rectangle:
    def __init__(self, color, length, width):
        self.color = color
        self.length = length
        self.width = width

    def area(self):
        self.area = self.length * self.width
        return self.area

    def perimeter(self):
        self.perimeter = 2*(self.length + self.width)
        return self.perimeter

    def diagonal(self):
        self.diagonal = (self.length**2 + self.width**2) ^ (1/2)
        return self.diagonal

    def volume(self, height):
        self.height = height
        self.volume = self.height * self.area()
        return self.volume


class Student:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
        self.grades = []

    def enterGrades(self):
        numGrades = int(input('How many grades are you entering? '))
        for i in range(0, numGrades, 1):
            grade = float(input(f"What was {self.firstName}'s grade? "))
            self.grades.append(grade)

    def totalGrade(self):
        total = 0
        for grade in self.grades:
            total += grade
        return total
    
    def averageGrade(self):
      return self.totalGrade()/len(self.grades)


tony = Student('tony','schwe')
tony.enterGrades();
print(tony.averageGrade());