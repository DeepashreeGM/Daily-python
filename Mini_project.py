class Student:
    college_name = "ABC Engineering College"   # Class variable
    student_count = 0                          # Class variable

    def __init__(self, name, roll_no, marks):
        self.name = name        # Instance variable
        self.roll_no = roll_no
        self.marks = marks

        Student.student_count += 1

    def display(self):
        result = "Pass" if self.marks >= 40 else "Fail"   # Local variable
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Marks:", self.marks)
        print("Result:", result)
        print("College:", Student.college_name)
        print("----------------------")


# -------- MAIN PROGRAM --------
students = []   # Global variable

while True:
    print("\n--- STUDENT MENU ---")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Total Student Count")
    print("4. Exit")

    choice = int(input("Enter your choice: "))   # Local variable

    if choice == 1:
        name = input("Enter name: ")      # Local variable
        roll = int(input("Enter roll no: "))
        marks = int(input("Enter marks: "))

        s = Student(name, roll, marks)
        students.append(s)

    elif choice == 2:
        for s in students:
            s.display()

    elif choice == 3:
        print("Total Students:", Student.student_count)

    elif choice == 4:
        print("Exiting program...")
        break

    else:
        print("Invalid choice")