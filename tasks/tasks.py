# """
# 1. Сгенерируйте рандомный пароль который будет следовать следующим требованиям: пароль должен содержать 2 символа верхнего регистра, одно число и один спец.символ. Подсказка: Используйте библиотеки random и string.
# """
# import random
# import string

# letter1 = random.choice(string.ascii_uppercase) 
# # print(string.ascii_uppercase)
# letter2 = random.choice(string.ascii_uppercase)
# number = random.randint(1,10) 
# simvol= random.choice(string.punctuation)
# # print(letter1, letter2 ,number, simvol)

# password = [letter1,letter2,str(number),simvol]
# random.shuffle(password)
# password= ''.join(password)
# print(password)


# a=5
# b=7
# c=78
# if a>b<c:
#   print(b)
# elif b>a<c:
#   print(a)
# elif a>c<b:
#     print(c)


# num = int(input())
# c = input("Перевести в байты (b) или килобайты (k): ")
# if c == 'b':
#     print(f'{num} Кб =  {num*1024} байт')
# elif c == 'k':
#     print(f'{num} байт = {num/1024} Кб' )