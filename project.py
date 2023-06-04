from datetime import datetime

# Функция для чтения данных из файла
def read_student_data(filename):
    group = []

    with open(filename, 'r') as file:
        lines = file.readlines()

        for line in lines:
            student_data = line.strip().split(',')

            student = {
                'фамилия': student_data[0],
                'имя': student_data[1],
                'дата_рождения': datetime.strptime(student_data[2], '%Y-%m-%d'),
                'зачетка': {
                    'предмет': student_data[3],
                    'дата_экзамена': datetime.strptime(student_data[4], '%Y-%m-%d'),
                    'преподаватель': student_data[5]
                }
            }

            group.append(student)

    return group

# Функция для вывода информации о студентах
def print_student_info(student):
    print(f"ФИО: {student['фамилия']} {student['имя']}")
    print(f"Дата рождения: {student['дата_рождения'].strftime('%Y-%m-%d')}")
    print(f"Зачетка:")
    print(f"  Предмет: {student['зачетка']['предмет']}")
    print(f"  Дата экзамена: {student['зачетка']['дата_экзамена'].strftime('%Y-%m-%d')}")
    print(f"  Преподаватель: {student['зачетка']['преподаватель']}")

# Функция для определения самого младшего и самого старшего студента
def find_youngest_and_oldest_students(group):
    youngest_student = None
    oldest_student = None

    for student in group:
        if youngest_student is None or student['дата_рождения'] < youngest_student['дата_рождения']:
            youngest_student = student
        if oldest_student is None or student['дата_рождения'] > oldest_student['дата_рождения']:
            oldest_student = student
    
    return youngest_student, oldest_student

# Чтение данных из файла
group = read_student_data('students.txt')

# Вывод информации о студентах
for student in group:
    print_student_info(student)
    print()

# Определение самого младшего и самого старшего студента
youngest, oldest = find_youngest_and_oldest_students(group)
print("Самый младший студент:")
print_student_info(youngest)
print()
print("Самый старший студент:")
print_student_info(oldest)
