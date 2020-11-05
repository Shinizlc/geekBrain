def sum_value(*args):
    s=0
    for num in args:
        s+=int(num)
    return s

def string_to_sum():
    result = 0
    while True:
        try:
            user_string=input('Enter the string of numbers or q for quit:\n')
            numbers=user_string.split(' ')
            result += sum_value(*numbers)
            print(result)
            #yield(result)
            #return result
        except ValueError:
            if user_string=='q':
                print('EXITING')
                break
            else:
                print('Enter the numeric values:\n')


string_to_sum()


