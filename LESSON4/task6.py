from itertools import cycle, count,islice
def list_generation(first_value:int,last_value:int,step:int=1)->list:
    """function for the creation of list of values"""
    result=[i for i in islice(count(first_value,step),last_value)]
    return result


print(list_generation(2,10,1))



#####

l=[1,2,3,4,5,6,67,8787,4334,4545]
print([i for i in islice(cycle(l),10)])
