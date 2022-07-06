# def sum_o_arts(a: int,b :int ,c:int ,d :int ) -> int: # A B C D параметры
#     '''Returns sum of all parameters'''
#     return a+b+c+d

# result =sum_o_arts
# print(type(result))
# print(result(5,10,15,20))



#-------------------------------------------------------
# Позиционные и именованные аргументы
# def printParams(a = None,b =None,c = None):
#     print(a,"is stored in param a")
#     print(b,"is stored in param b")
#     print(c,"is stored in param c")

# printParams(c = 3,  a =5)

# def sum_o_arts(a: int,b :int ,c:int ,d :int ) -> int: # A B C D параметры
#     '''Returns sum of all parameters'''
#     return a+b+c+d

# print(sum_o_arts(1,2,3,4)) # Позиционные аргументы(arguments)
# print(sum_o_arts(a=5,b=6,d= 7,c= 7)) # Именованные аргументы (keyword arguments)
# print(sum_o_arts(5,10,d =15,c=20)) 


#------------------------------------------------------------

# Оператор *

# a= [1,2,3]
# b = [4,5,6]
# c = [*a,*b]
# print(c)
# print(*a,end = "*\n")



#-----------------------------------------
# *args **kwargs в функциях



# def print_scores(student,*args):
#     print(f'Student name: {student}')
#     # print(args)
#     # print(type(args))
#     for x in args :
#         print(f'Оценка : ', x)

# print_scores('John Snow',100,14,41,44,44)


# def print_pat_names(owner,**kwargs):
#     print(f'Owner name: {owner}')
#     # print(kwargs)
#     # print(type(kwargs))
#     for x ,name in kwargs.items():
#         print(f'{x}:{name}')

# print_pat_names("John Snow",a="dog",b = 'cat', fish =['Nemo', 'Dory','Alex'],turtle = "Leonardo")



# def get_some_data(a,b ,*args,**kwargs):
#     print('параметры a and b: ' , a ,b)
#     print(args[0])
#     print(args[-1])
#     print(kwargs['name'])
#     print('Аргументы: ', args)
#     print('Именнованые аргументы: ', kwargs)

# get_some_data(1,2,3,4,5,lang = 'Python',name= "John Snow", car = 'BMW M5')


# def conc_two_string(str1,str2):
#     import random
#     res  = random.randint(1,10)
#     return str1 + str2 + str(res)
# result = conc_two_string('Hello', 'world')
# print(result)

#----------------------------------------------------------------------------------




# def ganerate_password(name,fam):
#     import random
#     random_num = random.randint(100000,999999)
#     return name + fam + '_' + str(random_num)

# def get_info():
#     name = input('Ввелите имя: ')
#     fam = input('Введите фамилию: ')
#     return ganerate_password(name,fam)

# result = get_info()
# print(result)

#----------------------------------------------------------------------------------


# def  generate_random_string(len_, lang):
#     import string as s
#     import random
#     random_str= ''.join(random.choice(s.ascii_lowercase + s.digits)for i in range(0,len_))
#     return random_str 
    
# print(generate_random_string(15,'eng'))

#----------------------------------------------------------------------------------




def add(num1,num2): return num1+ num2
   
def subtract(num1,num2):return num1-num2

def multiply(num1,num2): return num1*num2

def divide(num1,num2):
    try:
        return num1/num2
    except ZeroDivisionError:
        return 'На ноль делить нельзя!!!'

def main():
    try:
        num1 = float(input('Введите 1 число : '))
        num2 = float(input('Введите 2 число : '))
    except ValueError:
        print('Вы ввели некорректные данные')
        main()
    operator = input('Введите операцию (+,-,*,/): ')
    result = None
    if operator=="+": result = add(num1,num2)
    elif operator == '-': result = subtract(num1,num2)
    elif operator == '*': result = multiply(num1,num2)
    elif operator =='/': result = divide(num1,num2)
    else:  print('Вы ввели некорректный оператор!!!')

    print('Результат : ', result)
    question = input('Хотите продолжить?(Yes/No): ')
    if question.lower()== 'yes':
        main()
    else:
        print('Thanks for using our calculator, Bye Bye !!!')


main()
