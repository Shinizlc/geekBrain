class Stationery():
    def __init__(self,title):
        self.title=title
    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        print('Рисуем ручкой')
class Pencil(Stationery):
    def draw(self):
        print('Рисуем карандашом')
class Handle(Stationery):
    def draw(self):
        print('Рисуем маркером')

pen=Pen('Some Title')
print(pen.title)
pen.draw()
pencil=Pencil('Another title')
print(pencil.title)
pencil.draw()
handle=Handle('Another title')
print(handle.title)
handle.draw()