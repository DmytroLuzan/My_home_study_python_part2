def get_sum(a, b):
    """
    Возвращает суму аргументов |a| и |b|.
    :param a: Первий операнд
    :type a: int
    :param b: Вторий операнд
    :type b: int
    :return: Return type int
    """
    return a + b

# print(get_sum.__doc__)
# print(get_sum(1, 2))

# def f():
#     x = 5
#
# print(x)

a = 5 # global
#
# def f():
#     a = 10 # local
#     a += 1
#     print(a)
# print(a)
# f()
# print(a)

# def f():
#     global a
#     a += 1
#     print(a)
# print(a)
# f()
# print(a)

l = [1, '2', 3]

def f(l):
    return [i * 2 for i in l]

print(f(l))


def f2(l):
    def get_mult(x):
        return int(x) * 2
    return [get_mult(i) for i in l]

print(f2(l))


def f3(l):
    def get_mult(x):
        if isinstance(x, int):
            return x * 2
    return [get_mult(i) for i in l if get_mult(i)]

print(f3(l))


def f4(l):
    def get_mult(x):
        return x * 2
    return list(map(get_mult, l))

print(f4(l))


def generate_range(min, max, step):
    #    return list(range(min, max + 1, step))
    list_range = []
    new_value = min
    while new_value <= max:
        list_range.append(new_value)
        new_value = new_value + step

    #return list_range

    print(list_range)
generate_range(1, 15, 2)


