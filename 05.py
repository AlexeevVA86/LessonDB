class Stationery:
    def __init__(self, title ):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('Нарисовал: Привет!')


class Pencil(Stationery):
    def draw(self):
        print('Нарисовал: как жизнь?')


class Handle(Stationery):
    def draw(self):
        print('Нарисовал: Рад слышать!')


object_1 = Pen('Ручка')
object_2 = Pencil('Карандаш')
object_3 = Handle('Маркер')

object_1.draw()
object_2.draw()
object_3.draw()
