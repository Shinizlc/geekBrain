def sum_max(a:int,b:int,c:int)-> int:
    """calculation the sum of the two maximal numbers"""
    try:
        a=int(a)
        b=int(b)
        c=int(c)
        l=[]
        for i in a,b,c:
            l.append(i)
        l = sorted(l)
        max_1=l[-1]
        max_2=l[-2]
        return max_1+max_2
    except ValueError:
        print("The values should be numeric!")


if __name__=="__main__":
    print(sum_max(1,2,3))
