import os
import sys
with open('task1.txt', 'w') as file:
    while True:
        text=str(input('Enter the line or enter "exit":\n')+'\n')
        print(text)
        line=file.write(text)
        if text == 'exit\n':
            file.write('\n')
            break


##не могу реализовать break
