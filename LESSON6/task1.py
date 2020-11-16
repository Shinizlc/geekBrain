from time import sleep
class TrafficLight:
    def __init__(self):
        self.__color='RED'
    def running(self):
        print(self.__color)
        sleep(7)
        self.__color='YELLOW'
        print(self.__color)
        sleep(2)
        self.__color='GREEN'
        print(self.__color)



tl=TrafficLight()
tl.running()