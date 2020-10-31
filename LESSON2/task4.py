user_string = input('Enter the string: ')
for n, i in enumerate(user_string.split(' ')):
    print(f'The {n+1} word is : {i[0:10]}') ### почему работает с 10 не с 9?должно же быть как раз 10 символов
