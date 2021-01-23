class Data:
    def __init__(self,day,month,year):
        self.day=day
        self.month=month
        self.year=year
    @classmethod
    def date_extractor(cls,data):
        day,month,year=data.split('-')
        return cls(day,month,year)
    @staticmethod
    def date_validation(day,month,year):
        

data=Data.date_extractor('16-06-1986')
print(data.month)

    # @staticmethod
    # def date_validation():




