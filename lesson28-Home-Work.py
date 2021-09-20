"""
1. Дан массив. в вкотором среди прочих єлементов есть слово "odd" (нечетный).
Определите, есть ли в списке число, которое является индексом элемента "odd". Напишите функцию,
которая будет возвращать True или False, соответственно.
"""


def odd_ball(arr):
    value1 = arr.index("odd")
    value2 = arr.count(value1)
    return bool(value2)


print(odd_ball(["even", 4, "even", 7, "even", 55, "even", 6, "even", 10, "odd", 3, "even"]))  # True
print(odd_ball(["even", 4, "even", 7, "even", 55, "even", 6, "even", 9, "odd", 3, "even"]))  # False
print(odd_ball(["even", 10, "odd", 2, "even"]))  # True

"""
2. Напишите функцибю find_sum(n), где аргумент функции - это конечный элемент
последовательности включительно. Функция должна вернуть сумму всех чисел последовательности,
кратных 3 и 5. Попробуйте решить задачу двумя способами (один из способов в одну строчку
кода).
"""


def find_sum(n):
    new_list = []
    for n in range(n + 1):
        if n % 3 == 0 or n % 5 == 0:
            new_list.append(n)
    print(sum(new_list))


print(sum([n for n in range(10 + 1) if n % 3 == 0 or n % 5 == 0]))

find_sum(5)  # return 8 (3 + 5)
find_sum(10)  # return 33 (3 + 5 + 6 + 9 + 10)

"""
3. Дан список имен. Выберите в новый список только те имена, которые состоят из 4-х букв.
names = ["Ryan", "Kieran", "Mark", "John", "David", "Paul"] # ["Ryan", "Mark", "John", "Paul"]
"""


def get_names(names):
    new_list = []
    for x in names:
        if len(x) == 4:
            new_list.append(x)

    print(new_list)


names = ["Ryan", "Kieran", "Mark", "John", "David", "Paul"]

get_names(names)


# names = ['alex', 'rob', 'jhon']
#
# print('first way:')
# for name in names:
#     print(name)
#
# print('second way:')
# for x in range(len(names)):  # [0,1,2]
#     print(names[x])
#
# print('while loop:')
# i = 0
# while i < len(names):
#     print(names[i])
#     i += 1