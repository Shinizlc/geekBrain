l=[300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
def compare_elements(a:list)->list:
    for elem in range(0,len(l)-1):
        if l[elem]<l[elem+1]:
            yield l[elem+1]


result=compare_elements(l)
print(list(result))