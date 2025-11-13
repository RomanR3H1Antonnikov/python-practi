from operator import index
from os import remove

students = [
    {"Студент": "Roman", "grades": [80, 90, 78]},
    {"Студент": "Ivan", "grades": [95, 90, 97]},
    {"Студент": "Mishkan", "grades": [60, 70, 64, 40]},
    {"Студент": "Makson", "grades": [60, 75, 70]}
]

def calculate_average(grades):
    return round((sum(grades) / len(grades)), 1)


def get_status(average_grade):
    if average_grade >= 75:
        return "Успешен"
    else:
        return "Отстающий"


def new_student(student_info):
    students.append(student_info)
    all_grades_list.clear()
    for student in students:
        if "grades" in student:
            all_grades_list.extend(student["grades"])
            global_average_num = calculate_average(all_grades_list)
            average_grade = calculate_average(student["grades"])
            student["Средний балл"] = average_grade
            student["Статус"] = get_status(average_grade)
            print(f"""Добавлен новый студент!\n Данные студента:\n{about_student(student)}""")
            print("Обновлённый общий средний балл:", global_average_num)


def about_student(student):
    return f"""Студент: {student["Студент"]}\nСредний балл: {student["Средний балл"]}\nСтатус: {student["Статус"]}"""


def del_student(students):
    for student in students:
        if "Средний балл" in student:
            if student["Средний балл"] <= lowest_average_grade:
                del students[students.index(student)]


all_grades_list = []
global_average_num = 0
lowest_average_grade = 999
for student in students:
    if "grades" in student:
        all_grades_list.extend(student["grades"])
        global_average_num = calculate_average(all_grades_list)
        average_grade = calculate_average(student["grades"])
        student["Средний балл"] = average_grade
        lowest_average_grade = min(lowest_average_grade, student["Средний балл"])
        student["Статус"] = get_status(average_grade)
        del student["grades"]
        print(about_student(student))
print("Общий средний балл:", global_average_num)
new_student({"Студент": "Alice", "grades": [68, 90, 55, 94]})
del_student(students)
print(students)