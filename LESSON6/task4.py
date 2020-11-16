class Car:
    def __init__(self,speed,color,name,is_police):
        self.speed=speed
        self.color=color
        self.name=name
        self.is_police=is_police
    def go(self):
        print('The car has started to move')
    def stop(self):
        print('The car has stopped')
    def turn(self,direction):
        print(f'The car turned {direction}')
    def show_speed(self):
        print('The current speed of the car is : ' +str(self.speed))

car1=Car(60,'black','Tesla',0)
car1.show_speed()
print(car1.name)

class TownCar(Car):
    def __init__(self,speed,color,name,is_police):
        super().__init__(speed,color,name,is_police)
    def show_speed(self):
        if self.speed>60: print('the speed is over the limit')
class WorkCar(Car):
    def __init__(self,speed,color,name,is_police=False):
        super().__init__(speed,color,name,is_police)
    def show_speed(self):
        if self.speed>60: print('the speed is over the limit')
    # def test(self):
    #     super().turn('right')
class SportCar(Car):
    def __init__(self,speed,color,name,is_police=False):
        super().__init__(speed,color,name,is_police)

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)

work_car=WorkCar(120,'green','BMW',0)

sport_car=SportCar(120,'black','MCClaren')
print(sport_car.speed)