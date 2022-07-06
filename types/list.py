# list()- (Список массив) - изменяемый , последовательный тип данных , который из себя представляет коллекцию каких либо объектов.

# my_list = [1, 'string', False, None,[1,2,3]]
# print (my_list)
# print(type(my_list))

# #1. -> list(<iterable>)

# my_list  = list('Hello world')
# print(my_list)


# tuple_ =('banana', 'apple,', 'cherry')
# print (tuple_)
# print (type(tuple_))
# my_list  = list(tuple_)
# print(my_list)
# print(type(my_list))


# 2. range() -> Возвращает последовательность  элементов(числа )


# a = list(range(1, 100,2))
# print(a)



# 3. -> []

# my_list = []
# print(type(my_list))


# print(dir(list))

# append(element)- Добавляет элемент в конец списка

# list_ = [1,2,3]
# print(list_)
# list_.append(5)
# list_.append([1,2,3])
# print(list_)

# extend (element [iterable]) -> Расширяет список добавляя элемент в конец . 

# list_ = [1,2,3]
# list_.extend([1,2,3])
# print(list_)


# insert(<index>, <element>)-> Добавляяет  element по указанному index 

# list_ =[1,2,3,True]
# list_.insert( 1, [1,21 ,None ])
# list_.insert(3,121)
# print(list_)
# print(list_[5])
# print(list_[1][2])
# print(list_[1:3])
# print(len(list_))


# index(element,[stert, end])-> Возвращает индекс elementa 


# ls = [1,2,3,33,3,4,5,5,7,2, "hello"]
# print(ls.index(5,7))
# if "hello" in ls:
#     print(f'"hello" is in list: {ls.index ("hello")}')

# count(<elelment>) -> Возвращает кол-во вхождений element в списке 


# ls = [1,2,3,3,4,5,5,5,5,5,1]
# result = ls.count(66)
# print(result) 


# remove(element)-> удаляет element , но если такого элемента нет ,то выводит ошибку 

# pop([index])->удаляет и возвращает элемент по index , но если indexне указан , то удаляет последний элемент 

# ls = [5,1,2,3,4,5]
# # ls.remove(5)
# deleted = ls.pop(0)
# d=ls.remove(1)
# print(ls)
# print(deleted)
# print(d)


# sort([reverse=True /False],[key=<>])-> Сортирует список , елси в аргументах передан revers = True то список будет отсортирован в убывающем порядке

from audioop import reverse


# ls= [5,0,-2,-101,102,23,1]
# print(ls)
# ls.sort(reverse=True)
# print(ls)

# ls= ['hello', 'john','privet','London','as']
# ls.sort(key=len,reverse=True)
# print(ls)

# Изменение списка

# ls=[1,'h',3]
# ls[1]=2
# print(ls)


# Удаление
# del ls[-1]
# print(ls)


# s= ['helfsfsfsfslo']
# print(s[(len(s) + 1) // 2:] + s[:(len(s) + 1) // 2])ls='Makerse'
# print(ls[(len(ls)+1)//2:]+ls[:(len(ls)+1)//2])
