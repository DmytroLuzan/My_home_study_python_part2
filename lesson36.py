from _typeshed import Self


class A:
    property1 = 'Property 1'
    property2 = 'Property 2'
    name = 'guest'
#
#     def say_hi(self, name='guest'):
#         return 'Hi, ' + name
#
# a = A()
# b = A()
# # a.property1 = 'Property 1'
# # a.property2 = 'Property 2'
# # print(a)
# print(a.property1)
# print(a.say_hi('John'))
# print(b.say_hi())
#
    def say_hi(self, name=''):
        if name:
            return 'Hi, ' + name
        else:
            return 'Hello, ' + self.name

a = A()
b = A()
print(a.property1)
print(a.say_hi('John'))
print(b.say_hi())

# ------------

name = 'Dima'

def walk():
    print('I am walking')

# ------------

name = 'Marichka'

def walk():
    print('I am walking')

# ------------

name = 'Artem'

def walk():
    print('I am walking')

person = {
    'name': name,
    'walk': walk
}

person1 = {
    'name': 'Artem',
    'walk': walk
}

person2 = person1.copy()
person2['name'] = 'Dima'


person3 = person1.copy()
person3['name'] = 'Dima'

class Person:
    def __init__(self, name, city):  # constructor
        self.name = name
        self.city = city

    def sayHi(self):
        print('Hi!')


country = 'World'

person = Person()
person.country # 'Ukraine'
person.sayHi()

person1 = Person('Dima', 'Kyiv')
person1.country # 'Ukraine'

dydy = Person('Yacek', 'Lodz')

person = Person('Dima', 'Kyiv')

test = Person('First', 'Some')

class Person:
    def __init__(self, name, city):  # constructor
        self.name = name
        self.city = city

    def sayHi(self):
        print('Hi!' + self.name)

def sum(one, two):
    return one + two

sum(1,2)
sum(54,23)