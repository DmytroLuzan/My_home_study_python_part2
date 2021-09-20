s = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
s2 = set('hello')
s3 = {i for i in range(1, 11)}
s4 = {3, 5, 1, 6, 9, 0}
s5 = {}
s6 = set()
print(s)
print(s2)
print(s3)
print(s4)
print(s5)
print(s6)
    # for i in s:
    # print(i)

# nums = [1, 2, 3, 3, 1, 2, 4, 5]
# nums2 = set(nums)
# print(nums2)

a = set('abracadabra')
b = set('alacazam')
c = a - b # вичитание - убираем из а все букви, которие есть в b
d = a | b # обединение - букви или в |a| или в |b|
e = a & b # пересечение - букви и в |а| и в |b|
f = a ^ b # множество из єлементов - букви в |а| или в |b|, но не в обоих
print(a, b, c, d, sep='\n')

y = frozenset('hello')
# y.add('test')
# print(y)



