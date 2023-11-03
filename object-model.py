class Diary:
    def __init__(self, pages, marks):
        self.pages = pages
        self.marks = marks

    def display_info(self):
        return f"Diary - Pages: {self.pages}, Marks: {self.marks}"

class Subject:
    def __init__(self, name):
        self.name = name

    def show_info(self):
        return f"Subject: {self.name}"

class Student:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def get_student_info(self):
        return f"Student - Name: {self.name}, Surname: {self.surname}, Age: {self.age}"

d1 = Diary(9, 5)
diary_info = d1.display_info()

s1 = Subject("Math")
subject_info = s1.show_info()

st = Student("Azamatov", "Amantur", 18)
student_info = st.get_student_info()
