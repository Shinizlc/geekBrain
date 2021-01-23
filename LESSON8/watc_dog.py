# from watchdog.observers import Observer
# from watchdog.events import FileSystemEventHandler
# from time import sleep
# import os
# list_dir='/Users/saleksei/some_dir'
# class CheckLogs(FileSystemEventHandler):
#     def on_created(self, event):
#         list_of_files=os.listdir(list_dir)
#         for files in list_of_files:
#             file,ext=files.split('.')
#             if ext=='log':print(files)
#
#
#
# observer1=Observer()
# handler1=CheckLogs()
# observer1.schedule(handler1,list_dir,recursive=True)
# observer1.start()
# try:
#     while True:
#         sleep(5)
# except KeyboardInterrupt:
#     observer1.stop()
#     print('The observer was stopped')

#observer1.join()










# class Test:
#     l = []
#     def __init__(self,a):
#         self.a=a
#     def append_list(self,some_value):
#         Test.l.append(some_value)
# test1=Test('rere')
# test1.append_list('54545')
# test1.append_list('544343435')
# test2=Test('rere3232')
# print(test2.l)



###################################
# from watchdog.events import FileSystemEventHandler
# from watchdog.observers import Observer
# from time import sleep
# path='/Users/saleksei/some_dir'
# class CheckLogs(FileSystemEventHandler):
#     pattern1='ORA-'
#     pattern2='PS2-'
#     pattern3='PLS-'
#     def on_created(self,event):
#         len_dir=len(path)+1
#         path_file=event.src_path
#         file=path_file[len_dir:]
#         name,ext=file.split('.')
#         if ext=='log':
#             with open(path_file,'r') as link:
#                 for line in link.readline():
#                     if CheckLogs.pattern1 in line or CheckLogs.pattern2 in line or CheckLogs.pattern3 in line:
#                         print(f'ALERT!!!!{path_file} CONTAINS SOME SEVERE ERRORS')
#         else:
#             pass
#
#
# observer1=Observer()
# handler1=CheckLogs()
# observer1.schedule(handler1,path,recursive=True)
# observer1.start()
# try:
#     while True:
#         sleep(5)
# except KeyboardInterrupt:
#     observer1.stop()

#можно ли достучаться до @property функции без определения объекта

# class Test:
#     __trtr=43433111
#     def __init__(self,var):
#         self.__var = var
#         print('object was created')
#     @property
#     def get_a(self):
#         return Test.__trtr
#
# test1=Test(4343)
# print(test1.get_a)
#
########################################
# from watchdog.events import FileSystemEventHandler
# from watchdog.observers import Observer
# from time import sleep
#
# file_path='/Users/saleksei/watchdog'
# class my_handler(FileSystemEventHandler):
#     def on_created(self,event):
#         file_name=event.src_path
#         print(file_name)
#
#
#
#
#
#
# handler1=my_handler()
# observer1=Observer()
#
# observer1.schedule(handler1,file_path,recursive=True)
# observer1.start()
# while True:
#     sleep(5)




class Super_class:
    def __init__(self,name,last_name,age):
        self.name=name
        self.last_name=last_name
        self.age=age
    @property
    def print_name(self):
        return (f'{self.name} {self.last_name}')

# cl=Super_class('Alex','Semerikov',34)
# print(cl.print_name)

class inherit(Super_class):
    def __init__(self,name,last_name,age,manager_id):
        super().__init__(name,last_name,age)
        self.manager_id=manager_id
        print(super().print_name)

inh=inherit('Alex','Semerikov',34,4343335)