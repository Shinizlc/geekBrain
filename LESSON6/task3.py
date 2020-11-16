class Worker:
    def __init__(self,name,surname,position):
        self.name=name
        self.surname=surname
        self.position=position
        self._income={'wage':0,'bonus':0}

class Position(Worker):
    def __init__(self,name,surname,position,wage,bonus):
        super().__init__(name,surname,position)
        self._income['wage']=wage
        self._income['bonus']=bonus

    def get_full_name(self):
        print(f'The full name is {self.name} {self.surname}')
    def get_total_income(self):
        print('The total salary including the bonus is : '+ str(self._income['wage']+self._income['bonus']))

position1=Position('Alex','Stelson','dba',30,130)
position1.get_total_income()