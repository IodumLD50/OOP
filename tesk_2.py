'''Создайте класс Autobus, который наследуется от класса Transport.

Дайте аргументу Autobus.seating_capacity() значение по умолчанию 50.

Используйте переопределение метода.

Используйте следующий код для родительского класса транспортного средства:

[ ]
class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"Вместимость одного автобуса {self.name}  {capacity} пассажиров"
Ожидаемый результат вывода:

Вместимость одного автобуса Renaul Logan: 50 пассажиров'''


class Transport: 
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage   
    def seating_capacity(self, capacity):
        self.capacity = capacity
        return f"Вместимость одного автобуса {self.name}: {self.capacity} пассажиров" #.format(self.name, self.capacity)

class Autobus(Transport):
    def seating_capacity(self, capacity = 50):
        self.capacity = capacity
        return super ().seating_capacity (capacity = 50)
    
School_bus = Autobus("Renault Logan", 140, 1200)
print(School_bus.seating_capacity())