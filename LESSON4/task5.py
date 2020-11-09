from functools import reduce
result=reduce(lambda x,y:x*y,[i for i in range(100,1001)])
print(result)