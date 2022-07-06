# Встроенные функции 

# input()
# print()
# str()
# sum()
# list()
# len()
# divmod()
# globals()
# locals()
# min()
# max() ect.



# map()
# filter()
# lambda
# enumirate()


# Анонимные функции  ->lambda(такие же функции только без названия )
# Lambda функции могут принимать сколько угодно аргументов, но всегда возвращает только одно выражение

# def some_args(a,b):
#     res = a+b
#     return res

# def some_args1(a,b): return a+b

# print(some_args(12,4))
# print(some_args1(12,4))


# sum_arg = lambda a,b : a+b
# print(sum_arg(12,4))


# x = lambda a,b,c : a+b+c
# print(x(5,6,7))


# def myFunc(n):
#     return lambda a: a*n

# my_doubler = myFunc(2)
# my_tripler = myFunc(3)
# print(my_doubler(11))
# print(my_doubler(22))
# print(my_tripler(11))
# print(my_tripler(22))


# ls =['def', 'Ivan','John','',' ']
# new_list = sorted(ls, key = len)
# print(new_list) 

 








# map(function,Iterable) -> Применяет функцию к каждому элементу последовательности
#  и возвращает mapobject(итератор) с результатами



# Например, с помощью map можно выполнять преобразования элементов .Перевести все строки в верхний регистр:
# list_of_words = ['one', 'two', 'three', 'dict']
# res =  list(map(str.upper,list_of_words))
# print(res)
# res1 =  list(map(len,list_of_words))
# print(res1)



# ls = ['1','2','3','4']
# res = list(map(int,ls))
# print(res)

# names  = ['John', 'Jamie', 'Sansa', 'Tirion','Aibek']
# res = list(map(lambda x:f'Hello mr/mrs {x}', names))

# print(res)

# nums = [1,2,3,4,5]
# nums2 = [100,200,300,400,500]

# res  = list(map(lambda x,y : x*y , nums, nums2))
# print(res)

# dict_ = {1:2,3:4,5:6}
# res =  dict(map(lambda items:(items[0],str(items[1])), dict_.items()))
# print(res)














# filter(function,Iterable) -> Применяет  ко всем элементам iterable функцию которую мы передаем
#  и возвращает filterobject(итератор) с теми объектами , для которых функция вернула True.

# list_of_str = ['one','two','list', '', '100','1','50','john99']

# res  = filter(str.isdigit,list_of_str)
# print(res)
# for x in res:
#     print(x)


# ls = [10,11,102,213,314,515]
# res = list(filter(lambda x : x%2!=0,ls))
# print(res)



# ls = ['John', 'one', 'two', 'list','makers','ev.22', 'ono']

# res = list(filter(lambda x :len(x)>=4,ls))
# print(res)















# enumerate(Iterable)


# ls = ['str1','str2','str3']
# i=0
# for x in ls:
#     print(f'element {x}, index {i}')
#     i+=1

# for i,x in enumerate(ls):
#     print(f'element {x}, index {i}')

# new_ls = list(enumerate(ls))
# print(new_ls)


#--------------------------------------------------------
# zip(Iterales) -> Соединяет каждый элемент  интерируемых объктов между собой в тип данных tuple
# и возвращает это.

# list1 = [1,2,3]
# list2 = [100,200,300]
# res = list(zip(list1, list2))
# print(res)


# a = [1,2,3,4,5]
# b = [10,20,30,40]
# c = [100,200,300]

# res = list(zip(a,b,c))
# print(res)


# zip для создания словарей

# di_keys = ['hostname','location','vendor','model','IOS','IP']
# di_values = ['london_r1','21 New Globe Walk','Cisco','4451','15.4','10.255.0.1']
# res = dict(zip(di_keys,di_values))
# print(res)





# di_keys = ['hostname','location','vendor','model','IOS','IP']
# data = {
#     'r1':['london_r1','21 New Globe Walk','Cisco','4451','15.4','10.255.0.1'],
#     'r2':['london_r2','21 New Globe Walk','Cisco','4451','15.4','10.255.0.1'],
#     'sw1': ['london sw1','21 New Globe Walk','Cisco','3850','36.0.XE','10.255.0.101']
# }

# london_data = {}
# for key in data.keys():
#     london_data[key]=dict(zip(di_keys,data[key]))

# print(london_data)



#---------------------------------------------------------------------------------------
# all и any 

# all ->Возвращает True , если все элементы объекта истинна(или объект пустой)

# ls = [False,1,'stroks',True]
# print(all(ls))

# ip = '10.255.0.a.1'
# res = all(i.isdigit() for i in ip.split('.'))
# print(res)


# any -> Возвращает True если хоть 1 элемент истенный

# ls = [0,0,'', False,1]
# print(any(ls))



# def ignore_command(command):
#     '''
#     Функция проверяет есть ли в команде  слово из списка ignore. 
#     True - если есть. False - если нет такого слова.
#     '''
#     ignore = ['rm -rf', 'alias', 'reset']

#     for word in ignore:
#        if word in command:
#         return True
#     return False


# # print(ignore_command("subo root user "))
# command = 'sudo  configuration'
# if ignore_command(command):
#     raise Exception ('Invalid command')
# print('Vse ok!')


# ignore = ['rm -rf', 'alias', 'reset']
# command = 'subo reset configuration'

# if any([i  in command for i in ignore]):
#     raise Exception ('Invalid command')
# print('vse ok!')




#-----------------------------------------------------
# from random import choices
# from string import ascii_letters, digits
# from itertools import repeat

# # q_pass= int(input('Введите кол-во паролей: '))
# q_pass =1000000


# print({
#     f(choices(ascii_letters,k=10),choices(digits,k=5)) for f in repeat(lambda x,y:''.join(set((x+y))), q_pass)
# })




