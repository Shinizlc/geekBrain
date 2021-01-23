class Test:
    l=[]
    def __init__(self,val):
        self.val=val
        print(f'class was initiated {self.val}')
        print(self)
    @staticmethod
    def add_to_list(val):
        return Test.l.append(Test(val))
    def __str__(self):
        return f'object {self.val} was created'

for i in range(1,10):
    Test.add_to_list(i)

#print(Test.l)

# print(test1.l)
# print(test1)