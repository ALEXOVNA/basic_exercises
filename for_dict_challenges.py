import collections

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]

key = 'first_name'
name_students = []
frequency_name = []


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


get_higest_frequency_name(data_frequency_name=count_frequency_name(data_list=students))


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


def count_frequency_name_school_students(school_students_data):
    for class_student in school_students_data:
        school_students_class = class_student

        top_name_among_school_class = count_frequency_name(data_list=school_students_class)

        top_name_among_school_classes.append(get_higest_frequency_name(data_frequency_name=top_name_among_school_class))
    print(f'higest name among top name: {top_name_among_school_classes}')


count_frequency_name_school_students(school_students_data=school_students)


symbol_class = 'class'
type_entity = 'students'
person_attribute = 'first_name'


school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2в', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]

is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}

title_classes = [title_class.get(symbol_class) for title_class in school]


def count_gender_in_class(database_school):
    persons_name = []
    schooller_classes = [class_student.get(type_entity) for class_student in database_school]

    for class_schooler in schooller_classes:
        name_schooler_in_class = [person for person in class_schooler]
        persons_name_class = [name.get(person_attribute) for name in name_schooler_in_class]
        persons_name.append(persons_name_class)
    return persons_name


def check_person_gender(students_in_class=count_gender_in_class(school)):
    count_male = 0
    for one_class in students_in_class:
        male_persons = [is_male[person] for person in one_class]
        for male in male_persons:
            if male == True:
                count_male += 1
            all_students_class = len(male_persons)
        count_female = all_students_class - count_male
        print(f'мальчиков - {count_male}\nдевочек - {count_female}\n')


check_person_gender(students_in_class=count_gender_in_class(database_school=school))


