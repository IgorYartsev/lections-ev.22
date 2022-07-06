# Области видимости и пространства имен 



# Built- in (Встроенная ) - print, len , max , int 
# Global (Глоабальная) -  
# Enclosed (Нелокальная, nonlocal)
# Local(локальная облать видимости

# def print_list(some_list):
#     for i in some_list:
#         print(i)

# i = 'q'
# print_list([1,23,4,5,123])
# print(i)


# a = 10 #global
# print #built-in
# def hello(): #global
#     a = 'Hello world' # local
#     print(a, "local inside at func")


# hello()
# print(a, "global")



# x = 'global'
# print(x) # 1

# def enclosed():
#     x = 'enclosed'
#     def local():
#         x = 'local'
#         print(x) # 3 local
#     print(x) # 2 enclose
#     local() 
#     print(x)# 4 enclose

# enclosed()
# print(x) # 5 

# a = 'str'
# def func():
#     print(a)

# func()

# num = 10 
# def func():
#     def inner_func():
#         print(num)
#     inner_func()


# func()

# var = 100# global variable 

# def increment():
#     # var = var +1 # Try to update a global variable (using incriment - > var+=1)
#     print(var)

# increment()

# global - > позволяет изменять значение глобальной переменной находясь в локальной области видимости 
# nonlocal - > позволяет изменять значение нелокальной переменной находясь в локальной области видимости 
 
# var = 100

# def increment():
#     global var 
#     var += 1 

# print(var)
# increment()
# increment()
# print(var)

# def counter():
#     num =0
#     def incrementer():
#         nonlocal num
#         num+=1
#         return num 
#     return incrementer

# c = counter()
# print(c) #<function counter.<locals>.incrementer at 0x10dcdc4c0>
# print(c()) #1 
# print(c()) #2
# print(c()) #3
# c = counter()
# print(c()) # 1

# print(dir(__builtins__)





# print(abs (-15)) # Стандартный вызов встроенной функции 

# abs = 15 # Переопределяю встроенное имя  fbs  в глобальной области 
# del abs
# print(abs(-15))




# a = [[1,2,3],[3,3,5]]
# res = max([sum(x) for x in a])

# print(res)

        



# alice =[54,20,10]

# john =[10,35,15]

# def compareScores(a,j):
#     score_a = 0
#     score_j = 0
#     for i in range(0,len(a)):
#         if a[i]> j[i]:
#             score_a +=1
#         elif j[i]>a[i]:
#             score_j+=1
#         else:
#             pass
#     return{"Alice":score_a,"john":score_j}

# print(compareScores(alice,john))




# str_='pythoniiist'
# dict_ = {key:str_.count(key)for key in str_ }
# print(dict_)




