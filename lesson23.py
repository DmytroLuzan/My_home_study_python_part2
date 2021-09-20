# d = {}
# product1 = {'title': 'Sony', 'price': 100}
# product2 = dict(title = 'iPhone', price = 110)
# users = [
#     ['bob@gmail.com', 'Bob'],
#     ['Katy@gmail.com', 'Katy'],
#     ['John@gmail.com', 'John']
# ]
# d_users = dict(users)
# print(users)
# print(d_users)
# print(type(d))
# print(product1)
# print(product2)

# product3 = dict.fromkeys(['price1', 'price2', 'price3'], 50)
# print(product3)

# nums = {i: i + 1 for i in range(1, 10)}
# print(nums)

product1 = {'title': 'Sony', 'price': 100}
product2 = dict(title = 'iPhone', price = 110)

# print(product1['title2'])
# print(product1.get('title2', 'NO')) # if no key


# print(nums['1']) # Error
# print(nums[1]) # Ok

# for key in product1:
#     print(f'{key}: {product1[key]}')
#
# for key, value in product1.items():
#     print(key, value)

products = [
    {'title': 'Sony', 'price': 100},
    {'title': 'iPhone', 'price': 110},
    {'title': 'Samsung', 'price': 90}
]
print(products)

for product in products:
    print(product['title'], product['price'])
