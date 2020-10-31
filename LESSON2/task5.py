
my_list = [7, 5, 3, 3, 2]

print(my_list)
while True:
    # try:
    user_input = abs(int(input('Enter your value: ')))
    for k, i in enumerate(my_list):
        # print(k)
        # print(i)
        if user_input ==i:
            my_list.insert(k+1, user_input)
            print('po uslovi <')
            break
        elif user_input<i:
            print(k)
            print(user_input)
            my_list.insert(k + 1, user_input)
            print('po uslovi >')
            #my_list.append(user_input)

        else:
            pass
        # else:
        #     my_list.insert(0,user_input)
        #     print('po uslovi 0')
    print(my_list)
    # except ValueError:
    #     print('Enter the numeric value!')
    #     exit(255)
