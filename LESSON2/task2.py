l = []
while True:
    elem = input('Enter your value: ')
    if elem =='': ###почему не работает is None
        break
    l.append(elem)

for i in range(0,len(l)-1,2):
    l[i],l[i+1]=l[i+1],l[i]
print(l)
