from tkinter import *


class Student:
    def __init__(self, name, roll_number, grade, marks):
        self.name = name
        self.roll_number = roll_number
        self.grade = grade
        self.marks = marks

    def calculate_grade(self):
        if self.marks < 0 or self.marks > 100:
            return None
        elif self.marks >= 90:
            return 'A'  
        elif self.marks >= 80:
            return 'B'
        elif self.marks >= 70:
            return 'C'
        elif self.marks >= 60:
            return 'D'
        elif self.marks >= 50:
            return 'P'
        else:
            return 'F'


def add_student():
    name = name_entry.get()
    roll_number = roll_entry.get()
    marks_str = marks_entry.get()

    try:
        marks = float(marks_str)
    except ValueError:
        invalid_label.config(text="Invalid mark entry. Marks should be a number.")
        window.after(3000, clear_error_label)
        return

    new_student = Student(name, roll_number, "", marks)
    grade = new_student.calculate_grade()

    if grade is None:
        invalid_label.config(text="Invalid mark entry. Unable to calculate grade.")
        window.after(3000, clear_error_label)
        return

    new_student.grade = grade
    students.append(new_student)

    name_entry.delete(0, END)
    roll_entry.delete(0, END)
    marks_entry.delete(0, END)
    invalid_label.config(text="")


def display_student_info():
    roll_number = roll_entry.get()
    found = False

    invalid_label.config(text="")

    for student in students:
        if student.roll_number == roll_number:
            info_label.config(
                text=f"Name: {student.name}\nRoll Number: {student.roll_number}\nGrade: {student.grade}\nMarks: {student.marks}"
            )
            window.after(7000, clear_info_label)
            found = True
            break

    if not found:
        info_label.config(text=f"Student with roll number {roll_number} not found.")
        window.after(3000, clear_info_label)


def delete_student():
    roll_number = roll_entry.get()
    found = False

    invalid_label.config(text="")

    for student in students:
        if student.roll_number == roll_number:
            students.remove(student)
            info_label.config(text=f"Student with roll number {roll_number} deleted.")
            window.after(5000, clear_info_label)
            found = True
            break

    if not found:
        info_label.config(text=f"Student with roll number {roll_number} not found.")
        window.after(3000, clear_info_label)


def update_student_info():
    roll_number = roll_entry.get()
    found = False

    invalid_label.config(text="")

    for student in students:
        if student.roll_number == roll_number:
            new_name = name_entry.get()
            if new_name:
                student.name = new_name
            new_roll_number = roll_entry.get()
            if new_roll_number:
                student.roll_number = new_roll_number
            new_marks_str = marks_entry.get()
            if new_marks_str:
                try:
                    new_marks = float(new_marks_str)
                except ValueError:
                    invalid_label.config(text="Invalid mark entry. Marks should be a number.")
                    window.after(3000, clear_error_label)
                    return
                student.marks = new_marks
                student.grade = student.calculate_grade()
            info_label.config(text="Student information updated.")
            window.after(3000, clear_info_label)
            found = True
            break

    if not found:
        info_label.config(text=f"Student with roll number {roll_number} not found.")
        window.after(3000, clear_info_label)


def exit_program():
    window.destroy()


def clear_error_label():
    invalid_label.config(text="")


def clear_info_label():
    info_label.config(text="")


students = []

window = Tk()
window.title("Student Management System")
window.config(padx=50, pady=10)

roll_label = Label(window, text="Roll Number:")
roll_label.grid(row=0, column=0, padx=10, pady=5, sticky="E")

roll_entry = Entry(window)
roll_entry.grid(row=0, column=1, padx=10, pady=10)

name_label = Label(window, text="Name:")
name_label.grid(row=1, column=0, padx=10, pady=5, sticky="E")

name_entry = Entry(window)
name_entry.grid(row=1, column=1, padx=10, pady=10)

marks_label = Label(window, text="Marks:")
marks_label.grid(row=2, column=0, padx=10, pady=5, sticky="E")

marks_entry = Entry(window)
marks_entry.grid(row=2, column=1, padx=10, pady=10)

button_frame = Frame(window)
button_frame.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

add_button = Button(button_frame, text="Add Student", command=add_student)
add_button.pack(pady=5)

display_button = Button(button_frame, text="Display Student", command=display_student_info)
display_button.pack(pady=5)

update_button = Button(button_frame, text="Update Student", command=update_student_info)
update_button.pack(pady=5)

delete_button = Button(button_frame, text="Delete Student", command=delete_student)
delete_button.pack(pady=5)

exit_button = Button(button_frame, text="Exit", command=exit_program)
exit_button.pack(pady=5)

info_label = Label(window, text="")
info_label.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

invalid_label = Label(window, text="")
invalid_label.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

window.grid_columnconfigure(1, weight=1)

window.mainloop()
