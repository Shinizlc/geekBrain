d={1:'один',2:'два',3:'три',4:'четыре'}
with open('task4.txt','r') as file:
    with open('task4_converted.txt', 'w') as w:
        for lines in file.readlines():
            #print(lines)
            lines=lines.strip()
            str_num,_,num=lines.split(' ')
            for k,v in d.items():
                if k==int(num):
                    str_num=v
            w.writelines(str_num+' - ' +num+'\n')



