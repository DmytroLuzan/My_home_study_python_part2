from bs4 import BeautifulSoup
import urllib.request

req = urllib.request.urlopen('https://www.ua-football.com/sport')
html = req.read()

soup = BeautifulSoup(html, 'html.parser')
news = soup.find_all('li', class_='liga-news-item')

results = []

for item in news:
    title = item.find('span', class_='d-block').get_text(strip=True)
    desc = item.find('span', class_='name-dop').get_text(strip=True)
    href = item.a.get('href')
    results.append({
        'title': title,
        'desc': desc,
        'href': href,
    })

print(results)

f = open('news.txt', 'w', encoding='utf-8')
i = 1

for item in results:
    f.write(f'Новость № {i}\n\nНазвание: {item["title"]}\nОписание: {item["desc"]}\nСилка: {item["href"]}\n**********\n\n')
    i += 1

f.close()


a = 1
b = 2
print('a + b = ', a + b) # 'a + b = 3'
name = 'Dima'
age = 100
height = 200

print('My name is ' + name + 'and my age is ' + str(age) + 'and I have height ' + str(height) + '!')
print(f'My name is {name} and my age is {age} and I have height {height}!')
# 'My name is Dima and my age is 100 and I have height 200!'

def func(first, second):
    pass