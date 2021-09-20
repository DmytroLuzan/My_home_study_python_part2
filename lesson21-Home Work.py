words = ['мадам', 'топот', 'test', 'madam', 'word']
my_str = ['Око за око', 'А роза упала на лапу Азора', 'Около Миши молоко']

def check_str(my_str):
    newwords = []
    for word in my_str:
        revword = word[::-1].lower().replace(' ', '')
        if revword == word.lower().replace(' ', ''):
            newwords.append(word)
    print(newwords)
check_str(my_str)

# palindromes = []
# for word in word:
#     if word == word[::-1]:
#         palindromes.append(word)
### palindromes = [word for word in words if word ==word[::-1]]
# print('io', palindromes)

def check_palendrom(words):
    new_words = []
    for word in words:
        revword = ''
        for i in word:
            revword = i + revword
        if revword == word:
            new_words.append(word)
    print(new_words)
check_palendrom(words)

# palindromes = []
# for word in my_str:
#     word_r = word.replace(' ', '').lower()
#     if word_r == word_r[::-1]:
#         palindromes.append(word)
# print(palindromes)

l = list(range(1, 10))
l2 = list('hello')
print(l, l2)

s = '-'.join(map(str, l))
s2 = ','.join(l2)
print([s])
print(s2)
print(l, list(map(str, l)))
