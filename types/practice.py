# import random
# ls= ['Plov','Manty','Kuurdak','Lagman','Dymdama']

# p =0
# m =0
# k =0
# l =0
# d =0
# for i in range(0,100000):
#     choice = random.choice(ls)
#     print(choice)
#     if choice.lower()== 'plov':
#         p=p+1
#     elif choice.lower() =='manty':
#         m = m+1
#     elif choice.lower() =='kuurdak':
#         k= k+1
#     elif choice.lower() == 'lagman':
#         l+=1  
#     elif choice.lower() =='dymdama':
#         d = d+1  
# print(f'Plov:{p},\nManty :{m}\nKuurdak:{k}\nLagman:{l}')

# выявить победителя !!!!


# dict_ = {'Plov': p, 'Manty': m,"Kuurdak": k ,'Lagman': l,'Dymdama': d}
# # print(dict_)
# res = sorted(dict_.items() , key = lambda x:x[1])
# winner = res[-1]
# print(f'Победило блюдо {winner[0]} оно наброло {winner[1]} очков!!!')






# def dol(str_):
#     step =0
#     l=0
#     for x in str_:
#         if x.lower() in 'd':
#             step-=1
#         elif x.lower() in 'u':
#             step+=1
#         if step==0 and step<0:
#             l+=1
#     return l

 

# print(dol('UDDDUDUU'))



# def countingValleys(steps,path):
#     dolina = 0 
#     sea_level = 0
#     for x in path:
#         if x == "U":
#             sea_level+=1
#             if sea_level==0:
#                 dolina+=1
#         elif x=='D':
#             sea_level-=1
#     return dolina    

# print(countingValleys(100,'DUDUUUUUUUUDUDDUUDUUDDDUUDDDDDUUDUUUUDDDUUUUUUUDDUDUDUUUDDDDUUDDDUDDDDUUDDUDDUUUDUUUDUUDUDUDDDDDDDDD')    
# )





