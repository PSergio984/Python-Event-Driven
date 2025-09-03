class Student:

    def __init__(self, name, grade):
        self.name = name
        self.grades = grade

    def avgGrade(self):
        return sum(self.grades) / len(self.grades)

    def showGrades(self):
        print(f"\n--- Grades for {self.name} ---")
        for i, grade in enumerate(self.grades):
            print(f"  Grade {i+1}: {grade}")
        print(f"\n  Average grade: {self.avgGrade():.2f}")
        gradeCategory = lambda avg: 'A' if avg >= 90 else 'B' if avg >= 80 else 'C' if avg >= 70 else 'D'
        print(f"  Grade category: {gradeCategory(self.avgGrade())}\n")

class GradeManager:
    def __init__(self):
        self.students = []

    def addStudent(self, student):
        self.students.append(student)

    def displayAllStudents(self):
        print("\n--- Student List ---")
        for i, student in enumerate(self.students):
            print(f"  {i+1}: {student.name}")
        print()

def main():
    gradeManager = GradeManager()
    gradeManager.addStudent(Student("Lex", [80, 90, 90]))
    gradeManager.addStudent(Student("Pudidi", [80, 90, 97]))
    gradeManager.addStudent(Student("Jet", [100, 100, 75]))

    while True:
        print("\n=== Welcome to Student Manager ===")
        print("What would you like to do?")
        print("  1 - View Students\n  2 - Create Student\n  3 - Exit\n")

        while True:
            try:
                choice = int(input("Enter your choice (1-3): ").strip())
                if choice < 1 or choice > 3:
                    print("Error: Please enter 1, 2, or 3.")
                    continue
                break
            except ValueError:
                print("Error: Please enter a valid number.")

        if choice == 1:
            gradeManager.displayAllStudents()
            print('Which student would you like to choose?')
            while True:
                try:
                    choice = (int(input(f"Enter your choice (1-{len(gradeManager.students)}): ").strip())-1)
                    if choice < 0 or choice >= len(gradeManager.students):
                        print("Invalid choice! Please try again.\n")
                    else:
                        gradeManager.students[choice].showGrades()
                        break
                except ValueError:
                    print("Error: Please enter a valid number.")
        elif choice == 2:
            print("\n--- Add a New Student ---")
            studName = input("Enter student name: ")
            grades = []
            for i in range(3):
                while True:
                    try:
                        grade = int(input(f"Enter grade {i+1} (0-100): "))
                        if grade < 0 or grade > 100:
                            print("Error: Grade must be between 0 and 100. Please try again.")
                            continue
                        grades.append(grade)
                        break
                    except ValueError:
                        print("Error: Please enter a valid number.")
            gradeManager.addStudent(Student(studName, grades))
            print(f"Student '{studName}' added successfully!\n")
        elif choice == 3:
            print("Exiting Student Manager.\n")
            break


main()
