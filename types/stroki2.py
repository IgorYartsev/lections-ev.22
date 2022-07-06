# Методы строк


# dir() - Функция которая вытаскивает методы типов данных
from random import random


# print(dir(int))


# '<соединитель>'.join (<массив который нужно соединить>)- Соединяет массив из строк по соединителю в одну строку

# ls = ['milk',  'bread',  'water',  'apple', ]
# joined = ''.join(ls)
# print(joined)

# split(разделитель) - Дробит сроку по разделителю и возращает тип данных list. 


# text ='Milk, Bread, Water, Apple'
# splited = text.split(', ')
# print(splited)
# joined =', '.join(splited)
# print(joined)


# replace (<old value>, <new value>,[count]) -> Меняет в строке значение old na new value ,если вы укажетте count ,то он заменит count раз 


# text = 'ha ha ha ha'
# result = text.replace ('ha','La')
# print(result)
# print (text)




# strip()-> Убирает пробельные символы в началеи в конце.
# rstrip () В конце удаляет
# lstrip() В Начале  удаляет

# text = input ('Введите ФИО:')
# print(text.strip())  
# # print(text)
# result = text.lstrip()
# print(result)

# count('simbol') -> Считает количество вхождений <simbol> в строку

# text = 'Hello world ! I\'m from Earth!'
# result = text.count ('m')
# print(result)

# index ('<value>', [start ],[end])-> Он выводит индекс значения в value в нашей строке. 

# text = 'Hello world! This is Makers!'
# result = text.index('!')
# print(result)

# print (text.find ('!'))

# import random

# name = 'Makers'
# result = random.choice(name)
# print(result)



# s =  input ('Введите число месяца и мы вам скажем какое это время года:')
# if s == ('1'):
#     print ('Зима')
# elif s == '12':
#     print('Зима') 
# elif s == '2':
#     print('Зима')
# elif s == '3':
#     print('Весна')
# elif s == '4':
#     print('Весна')
# elif s == '5':
#     print('Весна')
# elif s == '6':
#     print('Лето')
# elif s == '7':
#     print('Лето')
# elif s == '8':
#     print('Лето')
# elif s == '9':
#     print('Осень')
# elif s == '10':
#     print('Осень')
# elif s == '11':
#     print('Осень')



