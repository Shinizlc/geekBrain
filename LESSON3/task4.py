def power(x:float,y:float)->float:
    return x**y
print(power(2,-3))
def power_2(x:float,y:float)->float:
    result=1
    for _ in range(0,y):
        result*=x
    return result

print(power_2(2,2))

