from Classes_parser import Parser

parser = Parser('https://www.ua-football.com/sport', 'news39.txt')
parser.run()
# print(parser.raw_html)
# print(parser.html)
print(parser.results)

