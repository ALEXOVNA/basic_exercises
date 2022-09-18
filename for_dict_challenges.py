import collections

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]

key = 'first_name'
# name_students = []
# frequency_name = []


# счетчик кол-ва повторений имени в списке
def count_frequency_name(data_list):
    students_name = [student.get(key) for student in data_list]
    frequency_name = collections.Counter(students_name).most_common()
    for name in range(len(frequency_name)):
        print(f'{frequency_name[name][0]}:{frequency_name[name][1]}')
    return frequency_name


def get_higest_frequency_name(data_frequency_name):
    higest_frequency_name = []
    for value in range(1, len(data_frequency_name)):
        if data_frequency_name[0][1] < data_frequency_name[value][1]:
            higest_frequency_name = data_frequency_name[value][1]
        else:
            higest_frequency_name = data_frequency_name[0][0]
    print(f'Highest frequency student name: {higest_frequency_name}\n')
    return higest_frequency_name


# get_higest_frequency_name(data_frequency_name=count_frequency_name(data_list=students))


school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],
    [  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]


top_name_among_school_classes = []
school_students_class = []


# счетчик кол-ва повторений имени в списке
def count_frequency_name_school_students(school_students_data):
    for class_student in school_students_data:
        school_students_class = class_student

        # список высокочастотных имен в разрезе одного класса исх-го списка
        top_name_among_school_class = count_frequency_name(data_list=school_students_class)

        # список имен высокочастотных имен в разрезе классов исх-го списка
        top_name_among_school_classes.append(get_higest_frequency_name(data_frequency_name=top_name_among_school_class))
    print(f'higest name among top name: {top_name_among_school_classes}')


count_frequency_name_school_students(school_students_data=school_students)

# the programm working with err:
# first top name not added to the list of results <top_name_among_school_classes>