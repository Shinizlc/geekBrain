user_string = input('Enter the string: ')
for n, i in enumerate(user_string.split(' ')):
    print(f'The {n+1} word is : {i[0:10]}')