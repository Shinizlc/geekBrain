from random import randint
with open('num_to_write.txt','w') as file:
    for _ in range(3):
        num=randint(1,20000)
        file.write(str(num)+' ')
with open('num_to_write.txt','r') as file_r:
    line=file_r.readline().rstrip()
    sum=0
    for numbers in line.split(' '):
         numbers=int(numbers)
         sum+=numbers
    print(sum)

