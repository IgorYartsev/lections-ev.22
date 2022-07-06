# JavaSkript Object Notation  -> JSON
# Единый формат хранения и передачи данных между компьютерами , сервисами, приложениями 
# и языками программирования через сеть Интернет.
# <filename>.json 


# {
#     "id":1,
#     'author': 'Jhon',
#     'posts':[]
# } #--- Это JSON , задача научится переводить JSON в Python Dict

#!!! 
# JS object == {}
# PY dict == {}
# JSON == {}

# Процессы Стериализации данных и их Десесриализация

# Стериализация(Запись данных в JSON) -> Это перевод python dict в JSON формат
# (либо сохранить все в файл , либо сохраняем просто как текстовые данные)

# dump - метод записывает объект Python в ФАЙЛ в формате JSON
# dumps - метод записывает объект Python в СТРОКУ в формате JSON


# Десесриализация(Чтение данных из JSON) -> Это процесс перевода из JSONa в Python dict



# load - метод который считывает файл в формате JSON и переводит его в объекты в Python
# loads - метод который считывает JSON в текстовом формате и переводит его в объекты в Python


#-----------------------------------------------------------------------------
#  Процесс десериализации
# import json
# from ntpath import join
# from urllib.request import urlopen

# data = urlopen('https://randomuser.me/api/')

# print(type(data))
# # print(data)
# generate_to_dict = json.load(data)
# print(generate_to_dict)
# print(type(generate_to_dict))


# with open('downApi.json','r')as file:
#     data = file.read()
#     # print(data)
#     # print(type(data))
#     user = json.loads(data)
#     print(user)
#     print(type(user))


#--------------------------------------------
# Процесс стеарилизация

# import json

# dict_ = {
#     'name':'John',
#     'lastname': 'Snow',
#     'status': True,
#     'wife': None,
#     'children': False
# }
# with open('new.json','w') as file:
#     json.dump(dict_,file)


# import json

# dict_ = {
#     'name':'John',
#     'lastname': 'Snow',
#     'status': True,
#     'wife': None,
#     'children': False
# }


# str_ =json.dumps(dict_)
# print(str_)
# print(type(str_))


#-----------------------------------------------------------------


