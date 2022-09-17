import collections

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]


# --- main function ---

def count_frequency_name():
    name_students = []
    key = 'first_name'

    for i in range(len(students)):
        name_students.append(students[i][key])
        frequency_name_students = collections.Counter(name_students).most_common()

    for i in range(len(frequency_name_students)):
        name = frequency_name_students[i][0]
        frequency = frequency_name_students[i][1]
        print(f'{name} : {frequency}')

    def print_format_high_frequency_item(sourse=frequency_name_students):
        highest_frequency_name = f'\nHighest frequency student name: {sourse[0][0]}'
        print(highest_frequency_name)

    print_format_high_frequency_item()

    return frequency_name_students

# --- main function ---


# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2



# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
# students = [
#     {'first_name': 'Вася'},
#     {'first_name': 'Петя'},
#     {'first_name': 'Маша'},
#     {'first_name': 'Маша'},
#     {'first_name': 'Оля'},
# ]


# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша


school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]


def count_frequency_name_among_classes():
    name_students_in_class = []
    key = 'first_name'

    for n in range(len(school_students)):
        name_students_in_class.append(school_students[n])
    # print(name_students_in_class)
    frequency_name_students = collections.Counter(name_students_in_class).most_common()
    print(frequency_name_students)

    # for i in range(len(frequency_name_students)):
    #     name = frequency_name_students[i][0]
    #     frequency = frequency_name_students[i][1]
    #     print(f'{name} : {frequency}')

    # def print_format_high_frequency_item(sourse=frequency_name_students):
    #     highest_frequency_name = f'\nHighest frequency student name: {sourse[0][0]}'
    #     print(highest_frequency_name)

    # print_format_high_frequency_item()

    # return frequency_name_in_class


count_frequency_name_among_classes()



# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2б', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}
# ???


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}
# ???

# count_frequency_name()