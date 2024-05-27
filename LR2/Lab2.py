#Реалізація типів вагонів (Прототип)
from abc import ABC, abstractmethod
import copy

# Абстрактний клас для вагонів
class Wagon(ABC):
    @abstractmethod
    def clone(self):
        pass

# Конкретні типи вагонів
class CoupeWagon(Wagon):
    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return "Купейний вагон"

class PlatzkartWagon(Wagon):
    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return "Плацкартний вагон"

class RestaurantWagon(Wagon):
    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return "Вагон-ресторан"

# Використання патерну Прототип
if __name__ == "__main__":
    original_coupe = CoupeWagon()
    clone_coupe = original_coupe.clone()
    print(f"Оригінал: {original_coupe}")
    print(f"Клон: {clone_coupe}")

###Створення складних конфігурацій поїздів (Будівельник)
from abc import ABC, abstractmethod

# Клас для представлення поїзда
class Train:
    def __init__(self):
        self.wagons = []

    def add_wagon(self, wagon):
        self.wagons.append(wwagon)

    def __str__(self):
        return f"Поїзд з вагонами: {', '.join(str(wagon) for wagon in self.wagons)}"

# Абстрактний клас-будівельник для поїздів
class TrainBuilder(ABC):
    @abstractmethod
    def add_wagon(self, wagon):
        pass

    @abstractmethod
    def get_train(self):
        pass

# Конкретний клас-будівельник для швидкісного поїзда
class HighSpeedTrainBuilder(TrainBuilder):
    def __init__(self):
        self.train = Train()

    def add_wagon(self, wagon):
        self.train.add_wagon(wagon)

    def get_train(self):
        return self.train

# Конкретний клас-будівельник для пасажирського поїзда
class PassengerTrainBuilder(TrainBuilder):
    def __init__(self):
        self.train = Train()

    def add_wagon(self, wagon):
        self.train.add_wagon(wagon)

    def get_train(self):
        return self.train

# Конкретний клас-будівельник для вантажного поїзда
class FreightTrainBuilder(TrainBuilder):
    def __init__(self):
        self.train = Train()

    def add_wagon(self, wagon):
        self.train.add_wagon(wagon)

    def get_train(self):
        return self.train

# Клас для керування процесом будівництва поїздів
class Director:
    def __init__(self, builder):
        self.builder = builder

    def construct_train(self, wagons):
        for wagon in wagons:
            self.builder.add_wagon(wagon)
        return self.builder.get_train()

# Використання патерну Будівельник
if __name__ == "__main__":
    # Використання патерну Прототип для створення вагонів
    coupe_wagon = CoupeWagon()
    platzkart_wagon = PlatzkartWagon()
    restaurant_wagon = RestaurantWagon()

    # Використання патерну Будівельник для створення поїздів
    high_speed_builder = HighSpeedTrainBuilder()
    director = Director(high_speed_builder)
    high_speed_train = director.construct_train([coupe_wagon.clone(), restaurant_wagon.clone()])
    print(high_speed_train)

    passenger_builder = PassengerTrainBuilder()
    director = Director(passenger_builder)
    passenger_train = director.construct_train([platzkart_wagon.clone(), coupe_wagon.clone()])
    print(passenger_train)

    freight_builder = FreightTrainBuilder()
    director = Director(freight_builder)
    freight_train = director.construct_train([restaurant_wagon.clone(), platzkart_wagon.clone()])
    print(freight_train)