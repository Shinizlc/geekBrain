user_num = int(input('Enter your number: '))
max_value = 0
while user_num > 0:
    last_figure = user_num % 10
    # print('last figure: '+ str(last_figure))
    # print('max value: ' +str(max_value))
    if last_figure > max_value:
        max_value = last_figure
        user_num = user_num // 10
    else:
        user_num = user_num // 10
print(max_value)
