l=[]
count=0
template={'Name':'Enter a name of an item: \n',
          'Price':'Enter the price: \n',
          'Quanitity':'Enter the quantity:\n '}


while count<10:###не получилось реализовать через while True.Каким образов организовать выход из цикла в данном случае
    d = {}
    for k, v in template.items():
        d[k] = input(v)
        # if d[k]=='':
        #     break
    l.append((count,d))
    count+=1
    print(l)


l_1=[]
dic_analyze={}
for i in l:
    dic=i[1]
    for j,m in dic.items():
        dic_analyze[j] = dic_analyze.get(j, []) + [m]
print(f'Aggregated data: ',dic_analyze)