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

# assert division(1,1)==1
# assert division(2,0)==None