class Student(object):
    """Represents a student."""

    def __init__(self, name, number):
        """All scores are initially 0."""
        self.name = name
        self.scores = [0] * number

    def getName(self):
        return self.name
  
    def setScore(self, i, score):
        self.scores[i - 1] = score

    def getScore(self, i):
        return self.scores[i - 1]
   
    def getAverage(self):
        return sum(self.scores) / len(self.scores)
    
    def getHighScore(self):
        return max(self.scores)
 
    def __str__(self):
        return "Name: " + self.name  + "\nScores: " + " ".join(map(str, self.scores))

    # Comparison methods
    def __eq__(self, other):
        return self.name == other.name

    def __lt__(self, other):
        return self.name < other.name

    def __ge__(self, other):
        return self.name >= other.name

def main():
    student1 = Student("Ken", 3)
    student2 = Student("Alice", 3)
    student3 = Student("Ken", 3)

    print("Student 1:", student1)
    print("Student 2:", student2)
    print("Student 3:", student3)

    print("\nComparisons:")
    print("student1 == student2:", student1 == student2)
    print("student1 == student3:", student1 == student3)
    print("student1 < student2:", student1 < student2)
    print("student2 >= student3:", student2 >= student3)

if __name__ == "__main__":
    main()

import random

def main():
    # Create multiple students
    students = [
        Student("Ken", 3),
        Student("Alice", 3),
        Student("Bob", 3),
        Student("Charlie", 3),
        Student("Diana", 3)
    ]

    # Set scores for variety (optional)
    for i, student in enumerate(students, start=1):
        for j in range(1, 4):
            student.setScore(j, 70 + i + j)  # Just some sample scores

    # Shuffle the list
    random.shuffle(students)
    print("Shuffled list of students:\n")
    for student in students:
        print(student, "\n")

    # Sort the list by student name
    students.sort()
    print("Sorted list of students by name:\n")
    for student in students:
        print(student, "\n")

if __name__ == "__main__":
    main()
