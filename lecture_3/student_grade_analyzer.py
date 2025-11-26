# Создаем пустой список для хранения данных о студентах.
# Каждый элемент списка - это словарь с ключами 'name' (имя) и 'grades' (список оценок).
students = []

def add_student():
# добавление нового студента в список
    name = input("Enter student name: ").strip()
    # Проверяем, существует ли уже такой студент по имени.
    if any(student['name'] == name for student in students):
        print(f"Student '{name}' already exists.")
    else:
        # Создаем новый словарь для студента с пустым списком оценок и добавляем его в общий список.
        new_student = {'name': name, 'grades': []}
        students.append(new_student)
        print(f"Student '{name}' added successfully.")

def add_grade():
# добавление оценок существующих стулентов
    name = input("Enter student name: ").strip()
    # Ищем студента в списке.
    found_student = None
    for student in students:
        if student['name'] == name:
            found_student = student
            break

    if found_student is None:
        print(f"Student '{name}' not found.")
        return

    print(f"Enter grades for {name} (enter 'done' to finish):")
    while True:
        grade_input = input("Enter a grade (or 'done' to finish): ").strip()
        if grade_input.lower() == 'done':
            break
        try:
            # Пробуем преобразовать ввод в целое число.
            grade = int(grade_input)
            # Проверяем, что оценка в допустимом диапазоне [0, 100].
            if 0 <= grade <= 100:
                found_student['grades'].append(grade)
                print(f"Grade {grade} added for {name}.")
            else:
                print("Invalid grade. Please enter a number between 0 and 100.")
        except ValueError:
            # Если не получилось преобразовать в число, выводим сообщение об ошибке.
            print("Invalid input. Please enter a number or 'done'.")

def calculate_average(student_grades):
# вспомогательная функция для расчета среднего балла и его возвращения
    if len(student_grades) == 0:
        return None
    return sum(student_grades) / len(student_grades)

def show_report():
# генерация полного отчета
    if len(students) == 0:
        print("No students have been added yet.")
        return

    # Список для хранения средних баллов каждого студента (если они есть).
    averages = []
    print("--- Student Report ---")

    for student in students:
        avg = calculate_average(student['grades'])
        if avg is None:
            print(f"{student['name']}'s average grade is N/A.")
        else:
            # Округляем до одного знака после запятой, как в примере.
            avg_rounded = round(avg, 1)
            print(f"{student['name']}'s average grade is {avg_rounded}.")
            averages.append(avg_rounded)

    # Если есть хотя бы один студент с оценками, выводим сводку.
    if len(averages) > 0:
        print("----------------------")
        max_avg = max(averages)
        min_avg = min(averages)
        overall_avg = sum(averages) / len(averages)
        print(f"Max Average: {max_avg}")
        print(f"Min Average: {min_avg}")
        print(f"Overall Average: {overall_avg:.1f}")

def find_top_performer():
# поск студента с самым высоким средним баллом
    # Фильтруем студентов, у которых есть оценки.
    students_with_grades = [s for s in students if len(s['grades']) > 0]

    if len(students_with_grades) == 0:
        print("No students with grades have been added yet.")
        return

    # Используем max() с лямбда-функцией, чтобы найти студента с максимальным средним.
    top_student = max(students_with_grades, key=lambda s: calculate_average(s['grades']))
    top_avg = calculate_average(top_student['grades'])

    # Округляем средний балл до одного знака.
    top_avg_rounded = round(top_avg, 1)
    print(f"The student with the highest average is {top_student['name']} with a grade of {top_avg_rounded}.")


def main():
# гдавная функция и запуск бесконечного цикла
    print("Student Grade Analyzer")

    while True:
        try:
            # Выводим меню.
            print("1. Add a new student")
            print("2. Add grades for a student")
            print("3. Generate a full report")
            print("4. Find the top student")
            print("5. Exit program")
            choice = input("Enter your choice: ").strip()

            # Обрабатываем выбор пользователя.
            if choice == '1':
                add_student()
            elif choice == '2':
                add_grade()
            elif choice == '3':
                show_report()
            elif choice == '4':
                find_top_performer()
            elif choice == '5':
                print("Exiting program.")
                break
            else:
                # Если введен неверный номер, сообщаем об этом.
                print("Invalid choice. Please select a number from 1 to 5.")
        except Exception as e:
            # На всякий случай ловим любые исключения, которые могут возникнуть в основном цикле.
            # Это делает программу более устойчивой к непредвиденным ошибкам.
            print(f"An unexpected error occurred: {e}")


# Запускаем программу.
if __name__ == "__main__":
    main()