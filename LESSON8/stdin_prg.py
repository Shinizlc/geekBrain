# class Name:
#     def __init__(self,f_name,l_name):
#         self.f_name=f_name
#         self.l_name=l_name
#     @classmethod
#     def full_name(cls,text):
#         f_name,l_name=text.split(' ')
#         return cls(f_name,l_name)
#     def print_full_name(self):
#         print(f'His/her name is {self.f_name} {self.l_name}')
#
# alex=Name.full_name('Alexei Semerikov')
# alex.print_full_name()

import subprocess as sb
import os
path=os.path.dirname(__file__)
command=path+'/stout_prg.py'
data='some data'
data=data.encode()
with sb.Popen(['python',command],stdout=sb.PIPE,stdin=sb.PIPE) as op:
        for line in op.communicate():
            print(line)




#
#
# result=sb.run(['ping','-t','5','ya.ru'],stderr=sb.PIPE,stdout=sb.PIPE)
# print(result.stdout.decode())

