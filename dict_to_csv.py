import csv

name_list = [
        {'name': 'Маша', 'age': 25, 'job': 'Scientist'}, 
        {'name': 'Вася', 'age': 8, 'job': 'Programmer'}, 
        {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
    ]

with open('export.csv', 'w', encoding = 'utf-8', newline = '') as f:
    fields = ['name', 'age', 'job', ]
    writer = csv.DictWriter(f, fields, delimiter = ';')
    writer.writeheader()
    for name in name_list:
        writer.writerow(name)
    