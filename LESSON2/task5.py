
my_list = [7, 5, 3, 3, 2]
print(my_list)
while True:
    try:
        user_input = abs(int(input('Enter your value: ')))
        for l in range(0,len(my_list)-1):
            v,v_1=my_list[l],my_list[l+1]
            if user_input <=v and user_input>=v_1:
                my_list.insert(l+1, user_input)
                break
            if user_input<min(my_list):
                my_list.append(user_input)

        print(my_list)
    except ValueError:
         print('Enter the numeric value!')
