# f = open('file.txt', encoding='utf = 8')
# text = f.read(2)
# text2 = f.read(8)
# print(f.encoding)
# text = f.read()
# f.close()

# print(text)
# print(text2)

# f = open('file.txt', 'a', encoding='utf-8')
# f.write('Нова строка\n')
# f.close()

# lines = ['Нова строка 1', 'Нова строка 2']
# f = open('file.txt', 'a', encoding='utf = 8')
# for i in lines:
#     f.write(i + '\n')
# f.writelines(lines)
# f.writelines(f'{i}\n' for i in lines)
# f.close()

# f = open('file.txt', 'r', encoding='utf = 8')
# for line in f:
#     print(line, end='')
##     print(line.replace('\n', ''))
# f.close

# lines = ['Nova stroka 1', 'Nova stroka 2']
# f = open('file1.txt', 'w', encoding='utf = 8')
# f.writelines(f'{i}\n' for i in lines)
# f.close

