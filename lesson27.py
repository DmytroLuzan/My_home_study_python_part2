# def get_sum(a, b, c, d):
#     return a + b + c + d
#
# print(get_sum(1, 2, 5, 7))

# args - позиционний аргумент
# kwargs- именнованние аргументи

# def get_sum(*args):
#     print(args)
# get_sum(1, 5, 10)
# print(sum([1, 2, 3]))

def get_sum(*args):
    return sum(args)
print(get_sum(1, 5, 10))

def func(**kwargs):
    print(kwargs)
func(a=1, b=5, c=20)

def f(a, x, *args, **kwargs):
    print(a)
    print(x)
    print(args)
    print(kwargs)

f(1, 2, 3, 4, b='test', c='hi')
f(1, 2)








