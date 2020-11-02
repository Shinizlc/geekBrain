first_val = int(input('Insert the the first value:'))
second_val = int(input('Insert the the second value:'))
k=0
while first_val<second_val:
    k+=1
    first_val=round(first_val+first_val*0.1,2)
    print(f' A day number {k} : {first_val}')
print(f'A sportsman will the results in {k} days')

