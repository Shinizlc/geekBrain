import os
dir=os.path.dirname(__file__)
file_path=os.path.join(dir,'task2.txt')

d={}
k=0
with open(file_path,'r') as file:
    for line in file.readlines():
        line=line.strip()
        k+=1
        print(k)
        for word in line.split(','):
            word=word.strip()
            d[word]=d.get(word,0)+1
        print(d)
