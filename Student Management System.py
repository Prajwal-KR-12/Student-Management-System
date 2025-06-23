# Function to validate roll number input
def get_valid_roll():
    while True:
        roll = input("Enter roll number (digits only): ")
        if roll.isdigit():
            return roll
        else:
            print(" Invalid input. Roll number must be numeric.")


# Student class
class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Roll No: {self.roll_no}, Name: {self.name}, Marks: {self.marks}")


# Manager class to handle student operations
class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self):
        roll = get_valid_roll()
        name = input("Enter name: ")
        marks = self.get_valid_marks()
        student = Student(roll, name, marks)
        self.students.append(student)
        print(" Student added successfully!")

    def display_students(self):
        if not self.students:
            print(" No student records found.")
            return
        for s in self.students:
            s.display()

    def search_student(self):
        roll = get_valid_roll()
        for s in self.students:
            if s.roll_no == roll:
                s.display()
                return
        print(" Student not found!")

    def update_student(self):
        roll = get_valid_roll()
        for s in self.students:
            if s.roll_no == roll:
                s.name = input("Enter new name: ")
                s.marks = self.get_valid_marks()
                print("Student updated!")
                return
        print(" Student not found!")

    def delete_student(self):
        roll = get_valid_roll()
        for s in self.students:
            if s.roll_no == roll:
                self.students.remove(s)
                print(" Student deleted!")
                return
        print(" Student not found!")

    def get_valid_marks(self):
        while True:
            try:
                marks = float(input("Enter marks (0-100): "))
                if 0 <= marks <= 100:
                    return marks
                else:
                    print(" Marks should be between 0 and 100.")
            except ValueError:
                print(" Please enter a valid number.")


# Main program loop
def main():
    sm = StudentManager()
    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            sm.add_student()
        elif choice == '2':
            sm.display_students()
        elif choice == '3':
            sm.search_student()
        elif choice == '4':
            sm.update_student()
        elif choice == '5':
            sm.delete_student()
        elif choice == '6':
            print("👋 Exiting program. Thank you!")
            break
        else:
            print(" Invalid choice. Please enter a number from 1 to 6.")


# Run the program
if __name__ == "__main__":
    main()
