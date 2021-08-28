# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    # atributes
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    # methods
    def go(self):
        return f'{self.name} has started'

    def stop(self):
        return f'{self.name} has stopped'

    def turn_right(self):
        return f'{self.name} has turned right'

    def turn_left(self):
        return f'{self.name} has turned left'

    def show_speed(self):
        return f'Current speed of {self.name} is {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'The speed of town car {self.name} is {self.speed}')

        if self.speed > 40:
            return f'Speed of {self.name} is higher than allowed for Towncar'
        else:
            return f'Speed of {self.name} is allowable for Towncar'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'The speed of Workcar {self.name} is {self.speed}')

        if self.speed > 60:
            return f'The speed of {self.name} is higher than allowed for Workcar'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} is PoliceCar'
        else:
            return f'{self.name} is not PoliceCar'


bmw = SportCar(100, 'Blue', 'BMW', False)
zaz = TownCar(30, 'Yellow', 'ZAZ', False)
vaz = WorkCar(70, 'Black', 'VAZ', False)
porsche = PoliceCar(110, 'White',  'PORSCHE 911', True)
print(vaz.turn_left())
print(f'When {zaz.turn_right()}, then {bmw.stop()}')
print(f'{vaz.go()} with speed {vaz.show_speed()}')
print(f'{vaz.name} is {vaz.color}')
print(f'Is {bmw.name} a police car? {bmw.is_police}')
print(f'Is {vaz.name}  a police car? {vaz.is_police}')
print(bmw.show_speed())
print(zaz.show_speed())
print(vaz.show_speed())
print(porsche.police())
print(porsche.show_speed())