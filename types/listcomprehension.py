# # 1 zadanie
# a = []
# for i in range(0,200):
        
#         if i %2 == 0:
#                 a.append(i)
# print(a)


# # 2 zadanie
# print('---------------------------------------------')
# a = []
# for i in range(0,200):
        
#         if i %2 == 0 and i %3 ==0:
#                 a.append(i)
# print(a)


# # 3 zadanie
# print('---------------------------------------------')
# a = []
# for i in range(0,100):
        
#         if i %2 == 0:
#                 b= i**2
#                 a.append(b)
#         elif i%2!=0:
#                 a.append(i)
# print(a)


# ---------------------------------------------------------------
# list comrehensions -> генераторы списков

# new_list = [expression for item in iterable  <if condition== True>  ]

# list - comprehension - > Это упрощенный подход к созданию списка, который задействует цикл for , 
# а также конструкции if-else для определения того что в итоге окажется добавлено в наш список.








# ls= []
# for i in range(0,100,2):
#     ls.append(i)
# print(ls) 


# new_list  = [i for i in range(0,100,2) ]
# print(new_list)


# ls = [i**2 for i in range(0,11)]
# print(ls)

# fruits  = ['apple', 'banana','kiwi','mango','limon']
# ls = [x.capitalize() for x in fruits]
# print(ls)
# ls = [x for x in fruits if 'a' in x]
# print(ls)

# ls = [x for x in fruits if x != 'apple']
# print(ls)

from io import IncrementalNewlineDecoder


list_ = [[1,2,3],[4,5,6],[7,8,9]]
# ls=[]
# for inner_ in list_:
#     for num in inner_:
#         ls.append(num)
# print(ls)

# ls = [x for inner_ in list_ for x in inner_ ]
# print(ls)


# import  datetime
# start = datetime.datetime.now()

# ls = [x for x in range(1,10000000) ]
# # ls = []
# # for x in range(1,10000000):
# #     ls.append(x)
# finish = datetime.datetime.now()
# print(finish - start)



# ls = [x for x in range(0,200) if x %2==0 and x%3==0]
# print(ls)

# ls = [x**2 if x%2==0 else x for x in range(0,100)]
# print(ls)

# ls = [x+10 if x==8 else x+1 for x in range(0,10)]
# print(ls)

