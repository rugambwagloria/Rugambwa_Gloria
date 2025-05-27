class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

class Student(Person):
    def __init__(self, name, age, student_id, course):
        super().__init__(name, age)
        self.student_id = student_id
        self.course = course

    def display_info(self):
        super().display_info()
        print(f"Student ID: {self.student_id}")
        print(f"Course: {self.course}")

class Lecturer(Person):
    def __init__(self, name, age, lecturer_id, department):
        super().__init__(name, age)
        self.lecturer_id = lecturer_id
        self.department = department

    def display_info(self):
        super().display_info()
        print(f"Lecturer ID: {self.lecturer_id}")
        print(f"Department: {self.department}")

class Staff(Person):
    def __init__(self, name, age, staff_id, position):
        super().__init__(name, age)
        self.staff_id = staff_id
        self.position = position

    def display_info(self):
        super().display_info()
        print(f"Staff ID: {self.staff_id}")
        print(f"Position: {self.position}")


if __name__ == "__main__":
    student = Student("Alice", 20, "S123", "Computer Science")
    lecturer = Lecturer("Dr. Smith", 45, "L456", "Mathematics")
    staff = Staff("Mr. Brown", 35, "ST789", "Administrator")

    print("Student Information:")
    student.display_info()
    print("\nLecturer Information:")
    lecturer.display_info()
    print("\nStaff Information:")
    staff.display_info()