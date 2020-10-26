input_data_sec = int(input('Enter the number of seconds: '))
sec=input_data_sec%60
minutes = input_data_sec//60
hours = minutes//60
print(f'{hours}:{minutes}:{sec}')