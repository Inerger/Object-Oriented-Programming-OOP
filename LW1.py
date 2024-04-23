from abc import ABC, abstractmethod

# Лабораторна робота 1:

# Фабричний метод для додавання типів потягів
class Train(ABC):
    @abstractmethod
    def __str__(self):
        pass

class HighSpeedTrain(Train):
    def __str__(self):
        return "Швидкісний потяг"

class PassengerTrain(Train):
    def __str__(self):
        return "Пасажирський потяг"

class FreightTrain(Train):
    def __str__(self):
        return "Вантажний потяг"

class TrainFactory:
    @staticmethod
    def create_train(train_type):
        if train_type == 'high_speed':
            return HighSpeedTrain()
        elif train_type == 'passenger':
            return PassengerTrain()
        elif train_type == 'freight':
            return FreightTrain()
        else:
            raise ValueError(f"Невідомий тип потяга: {train_type}")

# Абстрактна фабрика для вибору способу обслуговування
class Service(ABC):
    @abstractmethod
    def __str__(self):
        pass

class TechnicalService(Service):
    def __str__(self):
        return "Технічне обслуговування"

class PassengerService(Service):
    def __str__(self):
        return "Пасажирське обслуговування"

class ServiceFactory(ABC):
    @abstractmethod
    def create_service(self):
        pass

class TrainTechnicalServiceFactory(ServiceFactory):
    def create_service(self):
        return TechnicalService()

class TrainPassengerServiceFactory(ServiceFactory):
    def create_service(self):
        return PassengerService()

# Використання фабричного методу
if __name__ == "__main__":
    train_type = input("Введіть тип потяга (high_speed/passenger/freight): ")
    train = TrainFactory.create_train(train_type)
    print(f"Ви обрали: {train}")

    # Використання абстрактної фабрики
    if train_type == 'passenger':
        service_factory = TrainPassengerServiceFactory()
    else:
        service_factory = TrainTechnicalServiceFactory()

    service = service_factory.create_service()
    print(f"Обране обслуговування: {service}")
