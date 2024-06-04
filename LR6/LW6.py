### Парсинг та виконання команд на станції (Інтерпретатор)

from abc import ABC, abstractmethod

# Патерн Інтерпретатор
class Expression(ABC):
    @abstractmethod
    def interpret(self):
        pass

class ChangeTrackCommand(Expression):
    def interpret(self):
        print("Команда: Зміна колії")

class ArrivalCommand(Expression):
    def interpret(self):
        print("Команда: Прибуття потяга")

class DepartureCommand(Expression):
    def interpret(self):
        print("Команда: Відправлення потяга")

class CommandInterpreter:
    def interpret(self, command: str):
        if command == "change_track":
            return ChangeTrackCommand()
        elif command == "arrival":
            return ArrivalCommand()
        elif command == "departure":
            return DepartureCommand()
        else:
            raise ValueError(f"Невідома команда: {command}")

# Використання інтерпретатора
if __name__ == "__main__":
    interpreter = CommandInterpreter()

    commands = ["change_track", "arrival", "departure"]
    for command in commands:
        expression = interpreter.interpret(command)
        expression.interpret()

### Координація взаємодії між об'єктами станції (Посередник)

from abc import ABC, abstractmethod

# Патерн Посередник
class Mediator(ABC):
    @abstractmethod
    def notify(self, sender, event):
        pass

class StationMediator(Mediator):
    def __init__(self):
        self.dispatchers = []
        self.trains = []
        self.platforms = []

    def register_dispatcher(self, dispatcher):
        self.dispatchers.append(dispatcher)

    def register_train(self, train):
        self.trains.append(train)

    def register_platform(self, platform):
        self.platforms.append(platform)

    def notify(self, sender, event):
        if event == "train_arrived":
            print("Посередник: Потяг прибув. Повідомлення диспетчерів та платформ.")
            for dispatcher in self.dispatchers:
                dispatcher.update("train_arrived")
            for platform in self.platforms:
                platform.update("train_arrived")
        elif event == "train_departed":
            print("Посередник: Потяг відправився. Повідомлення диспетчерів та платформ.")
            for dispatcher in self.dispatchers:
                dispatcher.update("train_departed")
            for platform in self.platforms:
                platform.update("train_departed")

# Об'єкти, що взаємодіють через посередника
class Dispatcher:
    def __init__(self, mediator: Mediator):
        self.mediator = mediator
        self.mediator.register_dispatcher(self)

    def update(self, event):
        print(f"Диспетчер: Отримав повідомлення про {event}")

class Train:
    def __init__(self, mediator: Mediator):
        self.mediator = mediator
        self.mediator.register_train(self)

    def arrive(self):
        print("Потяг: Прибув на станцію.")
        self.mediator.notify(self, "train_arrived")

    def depart(self):
        print("Потяг: Відправляється зі станції.")
        self.mediator.notify(self, "train_departed")

class Platform:
    def __init__(self, mediator: Mediator):
        self.mediator = mediator
        self.mediator.register_platform(self)

    def update(self, event):
        print(f"Платформа: Отримала повідомлення про {event}")

# Використання посередника
if __name__ == "__main__":
    mediator = StationMediator()

    dispatcher1 = Dispatcher(mediator)
    dispatcher2 = Dispatcher(mediator)
    platform1 = Platform(mediator)
    platform2 = Platform(mediator)

    train = Train(mediator)
    train.arrive()
    train.depart()