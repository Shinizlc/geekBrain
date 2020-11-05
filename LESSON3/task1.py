# next=True
# while True:
#     answer = int(input('insert 1 or 0\n'))
#     if not answer:
#         next=False
#         break
#     else:
#         next=True
#
# # print(bool(int(0)))

#
# def print_dic(name,last_name):
#     return f'fullname: {name} {last_name}'
# dic=[{'name':'Aleksei','last_name':'Semerikov'},{'name':'Nikoloi','last_name':'Sovalev'}]
# l=[print_dic(**i) for i in dic if i['name']=='Aleksei']
# print(l)
# c = [1,2,3,4,5]
# def print_global():
#     #global c
#     c=[]
#     c.append('5454')
#     return c
#
# result=print_global()
# print(result)
# print(c)

def division (a:int,b:int)-> float:
    """function for division 2 numbers"""
    try:
        a=int(a)
        b=int(b)
        c=a/b
        return c
    except ValueError:
        print('wrong type, insert integer values')
    except ZeroDivisionError:
        print('enter the value of the denominator that is not equal to 0')


# result=division('8',1)
# print(result)

# print(division.__doc__)

assert division(1,1)==1
assert division(2,0)==None