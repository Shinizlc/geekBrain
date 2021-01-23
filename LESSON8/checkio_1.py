# def tupl(t:tuple)->tuple:
#     t_f=[]
#     t_f.append(t[0])
#     t_f.append(t[2])
#     t_f.append(t[-2])
#     return tuple(t_f)
#
# assert tupl((1,23,4545,7676,343))==(1,4545,7676)
#
# print(tupl((12,3545,7676,232,154,5)))


#
# def passwd_check(number:int)->int:
#     try:
#         return len(str((abs(int(number)))))
#     except ValueError:
#         print('Enter numeric value')
#
#
#
# print(passwd_check('323'))
#


# def sum_of_num(l:str)->int:
#     s=0
#     for words in l.split(' '):
#         if words.isdigit():s+=int(words)
#         else:continue
#     return s
#
#
# sum_of_num('test 123 and 321')



# def even_the_last(l:list)->int:
#     s=0
#     for i in range(0,len(l)-1,2):
#         s+=l[i]
#     s*=l[-1]
#     return s

#assert even_the_last([1,2,3])==12


#print(type(even_the_last([1,2,3,4,5,6])))
# import pymongo as pm
# connection=pm.MongoClient('127.0.0.1:27017')
# db=connection['test1']
# coll=db['test_collection']
# data=coll.find_one({'val':443433})
# print(data)


# def three_words_in_row(line:str)->bool:
#     '''check 3 words in row'''
#     k=0
#     for word in line.split(' '):
#         try:
#             if int(word):k=0
#         except:
#             k+=1
#             if k>=3:return True
#     return False
#
#
# assert three_words_in_row('bla bla bla bla bla')==True
# assert three_words_in_row('1 2 3 4')==False




# def even_last(l:list)->int:
#     sum=0
#     if len(l)>0:
#         for i in range(0,len(l),2):
#             sum+=l[i]
#         last_val=l[-1]
#         res=last_val*sum
#         return res
#     else:return 0
#
#
# assert even_last([1,2,3,4,5])==45
# import re
# l='..., test2 454'
#
# for i in re.split(', |. | ',l):
#     print(i)

# import datetime
# def diff_dates(t1:tuple,t2:tuple)->int:
#     birthday=datetime.date(t1[0],t1[1],t1[2])
#     today=datetime.date(t2[0],t2[1],t2[2])
#     res=today-birthday
#     return abs(res.days)
#
# #print(type(diff_dates((1982, 4, 19), (1982, 4, 22))))
# assert diff_dates((2014, 8, 27), (2014, 1, 1)) == 238




import requests as re
from bs4 import BeautifulSoup as bs
import wget
a=['https://www.pornpics.com/galleries/solo-model-amber-hahn-poses-in-sensual-lingerie-before-exposing-her-bald-twat/']
while True:
    data_link=a.pop()
    with re.get(data_link) as link:
        data=link.content.decode()
        data=bs(data)
        for tag in data.find_all('a'):
            l=tag.get('href')
            if l.startswith('https:') and l.endswith('jpg'):
                wget.download(l)


