class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = int(speed)
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
            print('Машина поехала.')

    def stop(self):
        print('Машина остановилась.')

    def turn(self, direction):
        print(f'Машина повернула на {direction}')

    def ShowSpeed(self):
        print(self.speed)


class TownCar(Car):
    speed = 70

    def ShowSpeed(self):
        if self.speed > 60:
            print('Превышение скорости!')


class SportCar(Car):
    car_model = 'Toyota'
    year = '1998'
    horse_power = 250


class WorkCar(Car):
    model = 'Iveco'
    transport = True
    longvehicle = True
    volume_can_take = 2
    speed = 60

    def ShowSpeed(self):
        if self.speed > 40:
            print('Превышение скорости!')


class PoliceCar(Car):
    model = 'Ford XB Interceptor w8'
    horse_power = 300
    transport = False
    patrol = False
    interceptor = True


Iveco_Dayli = WorkCar(55, 'Cosmic Grey', 'Iveco Dayli', False)
print(f'Cкорость автомобиля: {Iveco_Dayli.speed}\n'
      f'Цвет авто: {Iveco_Dayli.color}\n'
      f'Имя автомобиля: {Iveco_Dayli.color}\n'
      f'Машина полицейская?: {Iveco_Dayli.is_police}\n')

Iveco_Dayli.go()
Iveco_Dayli.turn('Право')
Iveco_Dayli.ShowSpeed()
Iveco_Dayli.stop()
