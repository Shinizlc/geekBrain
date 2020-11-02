###implementation via dictionary
while True:
    try:
        user_month = abs(int(input('Enter the number of month: ')))
        month_to_season={1:'winter',
        2:'winter',
        3:'spring',
        4:'spring',
        5:'spring',
        6:'summer',
        7:'summer',
        8:'summer',
        9:'fall',
        10:'fall',
        11:'fall',
        12:'winter'
        }
        for i in month_to_season.items():
            if i[0] == user_month:
                print(i[1])
    except:
        print('Wrong number of month. Enter the number from 1 to 12.')

#######
####implementation via list
while True:
    try:
        user_month = abs(int(input('Enter the number of month: ')))
        year=[(1,'winter'),(2,'winter'),(3,'spring'),(4,'spring'),(5,'spring'),(6,'summer'),(7,'summer'),
        (8,'summer'),(9,'fall'),(10,'fall'),(11,'fall'),(12,'winter')]
        for i in year:
            if user_month==i[0]:
                print(i[1])
    except ValueError:
        print('Wrong number of month. Enter the number from 1 to 12.')




