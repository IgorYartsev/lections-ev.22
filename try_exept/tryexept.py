# Отработка исключений
# Операторы: try .... except

# # Ошибки->связанные с кодом:


# SyntaxError
# IndentationError
# TabError 

# # Исключения  ->  Invalid Values
# ArithmeticError
# ZeroDivisionError
# NameError
# IndexError
# KeyError
# ValueError
# ImportError
# BaseException  # прородитель всех ошибок


# try .... except
# try:
#     <bode try>
# except:
#      <body except>



# num1 = int(input('Введите число:'))
# print(num1)
# print('очень важная строчка кода')

# try:
#     num1 = int(input('Введите число:'))
#     print(num1)
# except:
#     print('Вы ввели некорректные данные , исправьте это!!!!')

# print('очень важная строчка кода')


# 1. import sys
# list_= [ 1,2,3,4,5]
# index = int(input('Введите индекс: '))
# try: 
#     result = list_[index]
#     print(result)
# except :
#     import sys
#     print(f"Упс,мы на нашли{sys.exc_info()[0]}Error!!")

# 2. Exception as e 

# list_= [ 1,2,3,4,5]
# index = int(input('Введите индекс: '))
# try: 
#     result = list_[index]
#     print(result)
# except Exception as e:
#     print(f'Упс мы нашли {e.__class__} error!!' )


# list_= [ 1,2,3,4,5]
# try: 
#     index = int(input('Введите индекс: '))
#     result = list_[index]
#     print(result)
# except (IndexError, ValueError):
#     print('Вы ввели некорректные данные!!!!!!!')



# list_= [ 1,2,3,4,5]
# try: 
#     index = int(input('Введите индекс: '))
#     result = list_[index]
#     print(result)
# except IndexError:
#     print('Вы ввели некорректные данные IndexError')
# except ValueError:
#     print('Вы ввели некорректные данные ValueError')



# else в try ..... except 
# finaly в try ... except

# try:
#     <body>
# except:
#     <body>
# else:
#     <body>#Сработает  если в операторе не случилась ошибка
# finally:
#     <body> # Сработает при любом случае
# try:
#     num1 = int(input('Enter: '))
#     num2 = int(input('Enter2: '))
#     res= num1/ num2
# except ZeroDivisionError:
#     print('На ноль делить нельзя')
# except ValueError:
#     print('Invalid symbols!!!')
# else:
#     print(res)
# finally:
#     print('Код закончился!!!')