# l=[144,322,2121,322]
# def test_map(l):
#     for i in l:
#         yield i*2
#
# print(next(test_map(l)))


def factorial(n):
    l=[i for i in range(1,n+1)]
    print(l)
    result=1
    print(len(l))
    for k in range(0,len(l)):#(почему len(l) not len(l)-1 )
        result *= l[k]
        yield result

print(list(factorial(4)))
#1*2*3*4
# for i in factorial(4):
#     print(i)
#
# result=1
# for i in range(1,3):
#     result*=i
#     print(result)