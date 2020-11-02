revenue = int(input('Enter the profit amount: '))
expences = int(input('Enter the expences amount:'))
profit = revenue-expences
if profit > 0:
    print('The company has a profit: '+ str(profit))
    print('The profitability of the company is : '+ str(round(profit/expences)))
    emp_num = int(input('Enter the number of the employees: '))
    print('The profit per employee is '+ str(profit//emp_num))
else :
    print('The company has a loss!')


