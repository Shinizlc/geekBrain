# l=[]
# c=0
# template={'Name':'Enter a name of an item: \n',
#           'Price':'Enter the price: \n',
#           'Quanitity':'Enter the quantity:\n '}
#
#
# while True:
#     d = {}
#     for k, v in template.items():
#         d[k] = input(v)
#         # if d[k]=='':
#         #     break
#     l.append((c,d))
#     c+=1
#     print(l)
l=[(0, {'Name': 'comp', 'Price': '43', 'Quanitity': '3'}),
 (1, {'Name': 'calc', 'Price': '32', 'Quanitity': '2'})]
l_1=[]
dic_analyze={}
for i in l:
    dic=i[1]
    for j,m in dic.items():
        #dic_analyze[j] = (m)
        dic_analyze[j] = dic_analyze.get(j, []) + [m]
print(dic_analyze)