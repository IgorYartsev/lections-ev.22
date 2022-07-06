# def <name_of_function>(<a,b>#параметры) :
#     <body> # некий код, некая логика
#     <return> #возвращаем что то  
# <name_of _function >(<5, 6># арргументы)


# Параметры функции - переменные которые будут принимать наше функция ,  
# для того, чтобы мы смогли работать с данными, которые передаются в эту функцию


# Аргументы - это данные, которые мы передаем для параметров при вызове функции 


# Return - нужен для того , чтобы функция что то возвращала
#и для того чтобы мы могли работать с результатом действия функции , 
# return является необязательным оператором ( Возвращает None - если не указать return)


# ls = []
# res = ls.append(1)
# print(ls)
# print(res ,'результат дейсвия')

# res1 =ls.pop()
# print('результат дейсвия',res1)




# def sumTwoNums(num1,num2): # параметры
#     res = (num1 + num2)
    
#     return res

# print(sumTwoNums(5,5)) # аргументы


# def isEven(a):
#     if a%2 ==0 :
#         return True
#     else:
#         return False


# a = 10
# b= int(input("Enter num: "))

# print(isEven(4))
# print(isEven(a))
# print(isEven(b))



# def isEven1(num: int) -> bool:
#     '''
#     Наша функция проверяет является ли число, типа int,
#     четным
#     '''
#     if num%2 == 0:
#         return True
#     return False 

# isEven()
# isEven1()

# from typing  import List
# def get_polindron(words : List[str]) -> List:
#     '''
#     Функция возвращает список из полиндромов.
#     '''
#     result = []
#     for word in words:
#         if word.lower() == word[::-1].lower():
#             result.append(word)
#     return result


# some_words = ['John', 'Ono', 'Kazak', 'hello', 'Anna', 'walaw', ' kabak', 'Privet']

# print(get_polindron(some_words))


# def func():
#     print('Hello world')

# func()
#------------------------------------------------------
# default params

# def print_welcome(name:str = 'User') -> str:
#     print(f'Welcome,{name}!')

# print_welcome()


# '''
# Напишите функцию которая будет возвращать ваш депозит через определенное время с процентом 10
# возвращать финальное кол-во денег 
# Мин ставка денег 30к сомов 
# 2 параметра 

# '''




# def procent_year(num: float ,year: int) -> float:
#     '''
#     return final amount of money 
#     '''

#     if num <30000:
#         raise Exception('Вы ввели некорректное кол-во денег\n Мин ставка 30к ')
#     if year <3:
#         raise Exception ('Вы ввели некорректный срок  для депозита\n Мин период вложения 3 года')

#     i =0
#     while i< year:
#         num = num+ (num*0.1)
#         i +=1
#     return num 


# money = float (input('Введите сумму денег: '))
# year = int(input('Введите срок вашего депозита: '))

# print(procent_year(money ,  year))



# '''
# 'Hello world! My name is John, last name is Snow. Nice to meet you!'

# '''

# def get_reverse(stroka: str ) -> str :
#     '''
#     return reversed string:D
#     '''

#     ls = stroka.split()
#     a = list(reversed(ls))
#     l = ' '.join(a)
#     return l

# str_= 'Hello world! My name is John, last name is Snow. Nice to meet you !'

# print(get_reverse(str_))