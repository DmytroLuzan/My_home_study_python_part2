from datetime import date, datetime, timedelta
import locale

# today = date.today()
# print(today) # 2021-09-13
# print(today.day) # 13
# print(today.month) # 09
# print(today.year) # 2021
# print(today.weekday()) # 0 Monday

# # datetime
# now = datetime.now()
# # now2 = datetime.today()
#
# print(now) #(now2, sep='\n') # 2021-09-13 15:38:20.120694
# print(now.day) # 13
# print(now.month) # 09
# print(now.year) # 2021
# print(now.weekday()) # 0
# print(now.hour) # 15
# print(now.minute) # 50
# print(now.second) # 36
#
# days = ['пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'нд']
# print(days[now.weekday()]) # пн

locale.setlocale(locale.LC_ALL, 'ukr_UKR.UTF-8')
# #locale.setlocale(locale.LC_ALL, 'ua_UA')
#
# now = datetime.now()
# print()
#
# print(now.strftime('%a'))
# print(now.strftime('%A'))
# print(f'Дата: {now.strftime("%A, %d, %b, %Y")}')
# print(f'Время: {now.strftime("%H:%M:%S")}')
#
# print(now.strftime('%c'))
# print(now.strftime('%x'))
# print(now.strftime('%X'))

now = datetime.today()
print(now.strftime('%c'))
d1 = now + timedelta(days=1, hours=2, minutes=10)
print(d1.strftime('%c'))

os module
os.path


