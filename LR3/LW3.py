from abc import ABC, abstractmethod

# Патерн Стратегія
class ServiceStrategy(ABC):
    @abstractmethod
    def execute_service(self):
        pass

class TechnicalService(ServiceStrategy):
    def execute_service(self):
        print("Виконується технічне обслуговування")

class PassengerService(ServiceStrategy):
    def execute_service(self):
        print("Виконується обслуговування пасажирів")

class CargoService(ServiceStrategy):
    def execute_service(self):
        print("Виконується обслуговування вантажу")

class Train:
    def __init__(self, service_strategy: ServiceStrategy):
        self.service_strategy = service_strategy

    def perform_service(self):
        self.service_strategy.execute_service()

# Використання патерну Стратегія
if __name__ == "__main__":
    service_type = input("Введіть тип обслуговування (technical/passenger/cargo): ")
    if service_type == "technical":
        strategy = TechnicalService()
    elif service_type == "passenger":
        strategy = PassengerService()
    elif service_type == "cargo":
        strategy = CargoService()
    else:
        raise ValueError("Невідомий тип обслуговування")

    train = Train(strategy)
    train.perform_service()

##Реалізація системи оповіщення диспетчерів про статус потягів (Спостерігач)
from abc import ABC, abstractmethod

# Патерн Спостерігач
class Observer(ABC):
    @abstractmethod
    def update(self, event):
        pass

class TrainStatusNotifier:
    def __init__(self):
        self._observers = []

    def add_observer(self, observer: Observer):
        self._observers.append(observer)

    def remove_observer(self, observer: Observer):
        self._observers.remove(observer)

    def notify_observers(self, event):
        for observer in self._observers:
            observer.update(event)

class ArrivalObserver(Observer):
    def update(self, event):
        if event == "arrival":
            print("Сповіщення: Потяг прибув на станцію")

class DepartureObserver(Observer):
    def update(self, event):
        if event == "departure":
            print("Сповіщення: Потяг відправився зі станції")

class DelayObserver(Observer):
    def update(self, event):
        if event == "delay":
            print("Сповіщення: Потяг затримується")

# Використання патерну Спостерігач
if __name__ == "__main__":
    notifier = TrainStatusNotifier()

    arrival_observer = ArrivalObserver()
    departure_observer = DepartureObserver()
    delay_observer = DelayObserver()

    notifier.add_observer(arrival_observer)
    notifier.add_observer(departure_observer)
    notifier.add_observer(delay_observer)

    event = input("Введіть подію (arrival/departure/delay): ")
    notifier.notify_observers(event)

##Виконання команд для управління станцією (Команда)

from abc import ABC, abstractmethod

# Патерн Команда
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class TrainArrivalCommand(Command):
    def execute(self):
        print("Команда: Потяг прибув на станцію")

class TrainDepartureCommand(Command):
    def execute(self):
        print("Команда: Потяг відправився зі станції")

class ChangeTrackCommand(Command):
    def execute(self):
        print("Команда: Зміна колії")

class StationController:
    def __init__(self):
        self._commands = []

    def add_command(self, command: Command):
        self._commands.append(command)

    def execute_commands(self):
        for command in self._commands:
            command.execute()
        self._commands.clear()

# Використання патерну Команда
if __name__ == "__main__":
    controller = StationController()

    arrival_command = TrainArrivalCommand()
    departure_command = TrainDepartureCommand()
    change_track_command = ChangeTrackCommand()

    controller.add_command(arrival_command)
    controller.add_command(departure_command)
    controller.add_command(change_track_command)

    controller.execute_commands()
