# Есть два списка:
# tutors = [
#     'Иван', 'Анастасия', 'Петр', 'Сергей',
#     'Дмитрий', 'Борис', 'Елена'
# ]
# klasses = [
#     '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
# ]
#
#
# Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>), например:
# ('Иван', '9А')
# ('Анастасия', '7В')
# ...
#
# Количество генерируемых кортежей не должно быть больше длины списка tutors.
# Если в списке klasses меньше элементов, чем в списке tutors, необходимо вывести
# последние кортежи в виде: (<tutor>, None), например:
# ('Станислав', None)
#
# Доказать, что вы создали именно генератор. Проверить его работу вплоть до истощения.
# Подумать, в каких ситуациях генератор даст эффект.
tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б'
]


def tut_klas_gen(list_1, list_2):
    if len(list_1) <= len(list_2):
        for tutor, klass in zip(list_1, list_2):
            yield (tutor, klass)
    else:
        for index in range(len(list_2)):
            yield (tutors[index], klasses[index])
        while index < len(list_1):
            yield (tutors[index], None)
            index += 1


tut_klas_gen_1 = tut_klas_gen(tutors, klasses)
print(type(tut_klas_gen_1))
print(*tut_klas_gen_1, sep='')
