# dict() -> Словарь  -> это упорядоченная коллекция элементов (python 3.7 - > ordered ) Каждый элемент в словаре содержится в паре ключ : занчение .

# Ключи должны быть уникальными и должны быть неизменяемым типом данных (str, int, tuple,etc.)
# Тогда как значениями могуть выступать любые типы данных.





# thisdict = {
#     'brand': "Mustang",
#     'model': 'Mustang',
#     'year': 1964

# }
# print( type(thisdict))

# Hash tables ,ассоцивтивный массив ,dictionary, object(JS) == dictionary (py)


# a = {1,2,3} -> set 

# tuple_  = 1,2,3
# print (type(tuple_))
# print(tuple_)



# some_dict = {}
# print(type(some_dict))
# key_values = {'key': 'value', 'key1': 'value1'}
# print(type(key_values))
# dict_created_with_function = dict()
# print(type(dict_created_with_function))


# dict1 = dict((('key', 'value'), ('key2', 'value2')))
# print(dict1)
# print(type(dict1))
 
#  -----------------------------------------------------------------------------




# user_ifo = {
#     'first_name': "John",
#     'last_name': "Snow",
#     'age': 24,
#     'emails': 'johnsnow24@gmail.com',
#     'role': 'moderator',
#     'list':[1,2,3]
    # 'first_name': 'Raychel'
# }

# print(user_ifo['first_name'])
# print(user_ifo.get('age'))
# print(dir(dict))
# print(user_ifo.items())
# for items in user_ifo.items():
#     print(items)

# print(user_ifo.keys())#before changes
# user_ifo['age']=30
# print(user_ifo.keys())#after changes
# print(user_ifo)

# for keys in user_ifo.keys():
#     print(keys)


# for value in user_ifo.values():
#     print(value)


# pop()-> Удаляет элемент по определенному ключу 
# popitem() -> Удаляет последнюю пару в dict(словаре) 

# print(user_ifo)
# user_ifo.pop('list')
# user_ifo.pop('emails')
# user_ifo.popitem()
# print(user_ifo)

# setdefault(key, [default value]) - > Работает так же как и метод get() , но если такого ключа нет ,то он создает новую пару значений 

# 1 способ применения, получение значений 
# dict_ ={'name': 'John', 'age':23}
# result = dict_.setdefault('age')
# print(result)


# 2 способ применения, добавление пары 
# dict_ ={'name': 'John', 'age':23}
# result = dict_.setdefault('adress', 'Toktogula str.')
# print(dict_)


# print(user_ifo)

# user_ifo.update({'first_name':'Raychel'})
# user_ifo.update({'height': 185})
# print(user_ifo)

# ----------------------------------------------------

# roles = {
#     0:'Admin',
#     1:'Moderator',
#     2:'Vendor',
#     3:'Customer',
#     4:'Guest'
# }
# users = [
#     {
#         'id':0,
#         'name':'John',
#         'role': roles[0]
#     },
#     {
#         'id':1,
#         'name':'Raychel',
#         'role': roles[3]
#     },
#     {
#         'id':2,
#         'name':'Aibek',
#         'role': roles[4]
#     },

# ]

# product={
#     'id': 1,
#     'title': 'Samsung Galaxy S20',
#     'discription': 'Lorem Ipsum',
#     'prise': 1000
# }
# print(users)
# print(product)
# user_id = int(input('Введите ваш ID:'))
# if users[user_id]['role']==roles[0]:
#     product['discription'] =input('Введите новое описание продукта:')
# else:
#     raise Exception('У вас недостаточно прав !!')
# print(product)






user_ifo = {
    'first_name': "John",
    'last_name': "Snow",
    'age': 24,
    'emails': 'johnsnow24@gmail.com',
    'role': 'moderator',
    1:[1,2,3]
    
}
print(user_ifo.values())