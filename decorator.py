from abc import ABC
import math


class Vehicle(ABC):
    def __str__(self):
        return ''


class Car(Vehicle):
    def __init__(self, brand):
        self.brand = brand

    def __str__(self):
        return f'Машина бренда {self.brand}'

    def drive(self):
        return f'Да, машины бренда {self.brand} и такое имеют'


class Airplane(Vehicle):
    def __init__(self, capacity):
        self.capacity = capacity

    def __str__(self):
        return f'Самолет с вместимостью {self.capacity}'

    def fly(self):
        return f'Да, самолет с вместимостью {self.capacity} и такое умеет'


class AIVehicle(Vehicle):
    def __init__(self, vehicle, ai=False):
        self.vehicle = vehicle
        self.ai = ai

    def toggle_ai(self):
        self.ai = not self.ai

    def __str__(self):
        return f'{self.vehicle}{" не" if self.ai else ""} имеет ИИ управление'


car = Car('BMW')
print(car)
ai_car = AIVehicle(car)
print(ai_car)
ai_car.toggle_ai()
print(ai_car)
