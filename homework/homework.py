# # dict_ = {'persic':None, 'banana':200, 'arbuz':132, ' apple':505}
# # dic = {k:v for k, v in dict_.items() if v is not None}
# # print(dic)
# # for item in dict_:
# #     if dict_[item] is None:
# #         del dict_[item]

        
# # print(dict_)
#         # print(dict_[key])
# #    print(key, '->', dict_[key])





# # for values in dict_:
# #     # if i%2!=0:
# #         print(values)
    
    
# #   if i %2==0:
    
# # print(dict_)

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








# dict_ = {}
# def get_tolerance():
#   global dict_
#   dict_= {key:val  for key, val in dict_ if val<17 }

ls = [1,2,3,4,5]
print(list(map((filter(lambda x: x+1,ls),ls))))
