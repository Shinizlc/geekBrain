class zero_division(Exception):
    def __init__(self,txt=' '):
        self.txt=txt


def num_division(a,b):
    try:
        template={a:int(input('insert the first value: \n')),
                  b:int(input('insert the second value: \n'))}
        dic={}
        for k,v in template.items():
            dic[k]=v
    except:
        print('Wrong values,insert numeric values')
    try:
        if dic[b]==0:raise zero_division
        else:return dic[a]//dic[b]
    except zero_division:
        print('denominator shouldn"t be equal to zero, enter another value')

#assert num_division(4,2)==2 check the division

if __name__=="__main__":
    print(num_division(4,2))