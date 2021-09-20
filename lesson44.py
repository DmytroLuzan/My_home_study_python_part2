import re

# https://uk.wikipedia.org/wiki/%D0%A0%D0%B5%D0%B3%D1%83%D0%BB%D1%8F%D1%80%D0%BD%D0%B8%D0%B9_%D0%B2%D0%B8%D1%80%D0%B0%D0%B7

# https://docs.python.org/3.9/library/re.html

s = 'Єто просто строка кода. А єто еще одна строка текста.'
pattern = 'строка'
# print(pattern in s)
# print(s.find(pattern))

# if re.search(pattern, s):
#     print('Matched')
# else:
#     print('No match')
#
# match = re.search(pattern, s)
# print(match)
# print(match.start())
# print(match.end())
# print(match.span())

# print(re.match(pattern, s))

# print(re.findall(pattern, s))

# print(re.split(r'\.', s, 1))
# print(re.split(r'\.', s))

s = ''' Єто просто строка текста.
А єто еще одна строка текста.
А єто строка с цифрами: 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, , 10
А єто строка с разними символами: "!", "@", "-", "&", "?", "_"
a\\b\\tc
test string'''

# pattern = r'\w+' # r'\w'
# pattern = r'[єт]+' # r'[а-я]' r'[а-я0-9]' r'[а-яА-Я]'
# pattern = r'[0-9]+'
# pattern = r'\d+'
# pattern = r'[d-]+'
# pattern = r'a\\b\\tc'
# pattern = r'\w+$'
# pattern = r'^\w+'

# print(re.findall(pattern, s, flags=re.IGNORECASE)) # флагдля ігнора регістров

# mail@mail.com
# name@bank
# mail@google.com.ua


def validate_email(email):
    return bool(re.match(r'^.+@(\w+\.){0,2}[a-z]{2,6}$', email, re.IGNORECASE))

print(validate_email('mail@mail.com'))
print(validate_email('ivanov@bank'))
print(validate_email('mail@google.com.ua'))
print(validate_email('mail@google.com.info'))
print(validate_email('mail@google.com.infotest'))






