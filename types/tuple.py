# Tuple - это структура данных - 
# неизменяемый, 
# индексируемый , 
# упорядочный

# string1 = str('hello AttackPython')
# string2 = 'hello world'
# list1 = list(i for i in range(5))
# list2 = [1,2,3,4,5]
# set = {}
# dict1= {'key': "value"}


# tuple1 =(1,2,3)
# print(type(tuple1)) # - tuple class


# list1  = [1,2]
# list1[0] = 3
# tuple1 = 1,2
# tuple1[0] = 3 # Error!!!
# print(tuple1[0])
# print (tuple1[-1])
# print(type(tuple1))



# tuple1 = 1,2
# tuple2 = (1,)
# tuple3 = tuple([1,2,3])
# tuple4 = tuple(range(5))



# emails = ('Python@gmail.com','Tima@mail.ru',3,5,["potato",'arbuz','apple']) 

# # print(type(emails[-1]))
# last_object = emails[-1] # list 
# last_object.append('tomato')
# print (len(emails))


# print(dir(tuple)) - всего 2 метода


# tuple_sequnce_first = (2 , 2, 3, 4)
# tuple_sequnce = tuple(range(5))

# tuple_sequnce +=tuple_sequnce_first

# for value in tuple_sequnce:
#     print(value)



# names = ('Tima','Zhanylai','aidana','Bermet','Ermek')
# names_enter = ["Bermet",'Ermek']
# for name in names :
#     if name.capitalize() in names_enter:
#         print(f'hello {name.capitalize()}!!!')
#     # print('it is len:', len(name))
#     else:
#         print(f'{name} go home !!!')



# print(names[0]+ ' hello!')



# print(tuple_sequnce.count(2))
# indx = tuple_sequnce.index(4)
# print(tuple_sequnce[indx])



# first_step_names = []

# names = input('Enter names:').split(' ')

# for name in names:
#     if len(name)>4:
#         first_step_names.append(name)
        
# print(first_step_names)

# print('start for ')
# for i in range(10):
#     print(i)
# print('stop for')

# while 3>2:
#     print('i work')

# i=0
# num = 3
# while num>i:
#     print('i work')
#     i+=1



# b = []
# c = tuple(range(11))
# a= list(c)
# b = a
# print (b)

# b = []
# for i in range(1,11):
#   b.append(i)
# print (b)

# n=int(input())
# d=str(n//86400)
# h=str(n//180000)
# m=str((n//60)%60)
# s=str(n%60)
# print(d+':'+h+':'+m+':'+s)

