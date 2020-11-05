def get_user_info():
    template={'name':'Enter your first name:\n',
              'last_name':'Enter your last name:\n',
              'year':'Enter your first birth year:\n',
              'city':'Enter your the city of residence:\n',
              'email':'Enter your email:\n',
              'phone':'Enter your phone number:\n',}
    d={}
    for k,v in template.items():
        d[k]=input(v)
    return d

result=get_user_info()




def user_info(**kwargs):
    for k,i in kwargs.items():
        print(f'The {k} of the user in {i}')

user_info(**result)

