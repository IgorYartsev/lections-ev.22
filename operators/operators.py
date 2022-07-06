# Операторы сравнения
# условные операторы
# Логиеские операторы


# Операторы сранения:
# <,>,==(равно),>=,<=,!=(не равно)


# num1=18
# num2=15
# stroka1= 'h'
# print(ord(stroka1))
# stroka2= 'a'
# print(ord(stroka2))
# result =stroka1 > stroka2
# print (result)
# print(chr(1900))

# bool---True(1) or False(0)

# Условные операторы 
# if
# elif
# else


# if <condition>:
#    если в if приходит True
#     <body if>
# elif(else if) <condition>:
#     <body>
# else:
#     <body>


# string = input('Enter smt:')
# if string == 'Hello':
#     print("Hello srtranger!")
# elif string == 'Mersedes':
#     print('Mersedes Benz S class')
# else:
#     print('Совпадений не найдено')
# print('Код закончился')


# sign up 
# email = input('Enter email:')
# password1 = input('Enter password:')
# password2 = input('Enter password confirmation:')
# if password1 !=password2:
#     raise    Exception('Password didn\'t match!!!')
# else:
# #     print('Successfully singned Up!')
# age =input('Enter your age:')
# # print (type( age))1
# if age.isdigit():
#     age = int(age)
# else:
#     print('Введите корректные данные ')
#     raise Exception('Value error!')

# if age < 18:
#     print (f'Чувак приходи через {18 - age} года/лет')
# else:
#     print('Вы подходите по возрасту ')


# Логические операторы
# 1. and-> логическая и 
# 2.or-> логическая или
# 3. not-> логическое отрицание

# my_age= 20
# your_age =18
# result = my_age==20 and (your_age ==20)
# print(result)
# result = my_age>18 or your_age==20
# print(result)
# result = not my_age != 23
# print(result)


# is_user_google_user= True
# is_user_github_user= True 
# is_user_age_greater_21= False
# user_accounts_coins= 8000
# if (is_user_google_user and is_user_github_user) and (is_user_age_greater_21 or user_accounts_coins>5000):
#     print('You can enter the system mr John Snow')

# else:
#     print('Sorry, you should have Google and Github accounts! ')
# a = int(input('Введите число от 1 до 100:'))
# if a >=90:
#   print ('Отлично ваша оценка 5')
# elif a >=80:
#   print('Здорово ваша оценка ')
# elif a>=70:
#   print ('Хорошо ваша оценка 3')
# elif a>= 60:
#   print('Вам стоит подучить материал')
# else:
#   print('вы не сдали экзамен')


# count = 0

# a= input('Вввод целого числа')
# b= a.isdigit()
# if b== True:
#   count = int(a) 
#   print(count)
# else:
#   print ('нету цифры ')

# a = ''
# b = a.isdigit()
# print(b)




# a = '#qeqwe#rwerwe####'
# print(a.strip('#'))


