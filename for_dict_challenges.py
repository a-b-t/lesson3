# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Петя'},
]

from collections import Counter
list_students = []
for name in students:    
    a = name.get('first_name')
    list_students.append(a)
c = Counter(list_students)
for name in c:
    print(name, c[name])
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Оля'},
]
list_students = []
for name in students:    
    a = name.get('first_name')
    list_students.append(a)
c = Counter(list_students).most_common(1)
print(f'Самое часте имя среди учеников: {c[0][0]}')


# Пример вывода:
# Самое частое имя среди учеников: Маша

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
school_students = [
  [  # это – первый класс
    {'first_name': 'Вася'},
    {'first_name': 'Вася'},
  ],
  [  # это – второй класс
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
  ]
]
list_students = []
n = 0
for cl in school_students:
    n +=1    
    for name in cl:
        a = name.get('first_name')
        list_students.append(a)
        c = Counter(list_students).most_common(1)
    print(f'Самое частое имя в классе {n}: {c[0][0]}')
    list_students = []
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
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

for cl in school:
    num_male = 0
    num_female = 0
    num_class = cl.get('class')
    student = cl.get('students')
    for name in student:
        name_stud = name.get('first_name')
        if is_male[name_stud] == True:
            num_male += 1
        else:
            num_female += 1
    print(f'В классе {num_class} {num_female} девочки и {num_male} мальчика')


# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.
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
num_male_class = {}
num_female_class = {}
for cl in school:
    num_male = 0
    num_female = 0
    num_class = cl.get('class')
    student = cl.get('students')
    for name in student:
        name_stud = name.get('first_name')
        if is_male[name_stud] == True:
            num_male += 1
        else:
            num_female += 1
    num_male_class.update({num_class: num_male})
    num_female_class.update({num_class: num_female}) 
a = max(num_male_class, key = num_male_class.get)
b = max(num_female_class, key = num_female_class.get)
print(f'Больше всего мальчиков в классе {a}')
print(f'Больше всего девочек в классе {b}')
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a