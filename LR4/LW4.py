from abc import ABC, abstractmethod

# Патерн Команда
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

# Окремі команди
class ChangeTrackCommand(Command):
    def execute(self):
        print("Команда: Зміна колії")

class NotifyDispatcherCommand(Command):
    def execute(self):
        print("Команда: Повідомлення диспетчера")

class CheckWagonsCommand(Command):
    def execute(self):
        print("Команда: Перевірка вагонів")

class AnnounceDepartureCommand(Command):
    def execute(self):
        print("Команда: Оголошення про відправлення потяга")

class CheckTrainStatusCommand(Command):
    def execute(self):
        print("Команда: Перевірка стану потяга")

class ReleaseTrainCommand(Command):
    def execute(self):
        print("Команда: Випуск потяга на колію")

# Макрокоманди
class MacroCommand(Command):
    def __init__(self):
        self._commands = []

    def add_command(self, command: Command):
        self._commands.append(command)

    def execute(self):
        for command in self._commands:
            command.execute()

class TrainArrivalMacroCommand(MacroCommand):
    def __init__(self):
        super().__init__()
        self.add_command(ChangeTrackCommand())
        self.add_command(NotifyDispatcherCommand())
        self.add_command(CheckWagonsCommand())

class TrainDepartureMacroCommand(MacroCommand):
    def __init__(self):
        super().__init__()
        self.add_command(AnnounceDepartureCommand())
        self.add_command(CheckTrainStatusCommand())
        self.add_command(ReleaseTrainCommand())

# Використання макрокоманд
if __name__ == "__main__":
    arrival_macro = TrainArrivalMacroCommand()
    print("Виконується макрокоманда прибуття потяга:")
    arrival_macro.execute()

    departure_macro = TrainDepartureMacroCommand()
    print("Виконується макрокоманда відправлення потяга:")
    departure_macro.execute()

###Реалізація процесу обслуговування потяга (Шаблонний метод)

from abc import ABC, abstractmethod

# Патерн Шаблонний метод
class TrainService(ABC):
    def perform_service(self):
        self.check_documents()
        self.perform_specific_service()
        self.finalize_service()

    def check_documents(self):
        print("Перевірка документів")

    @abstractmethod
    def perform_specific_service(self):
        pass

    def finalize_service(self):
        print("Завершення обслуговування")

class TechnicalService(TrainService):
    def perform_specific_service(self):
        print("Виконується технічне обслуговування потяга")

class PassengerService(TrainService):
    def perform_specific_service(self):
        print("Виконується обслуговування пасажирів")

# Використання шаблонного методу
if __name__ == "__main__":
    service_type = input("Введіть тип обслуговування (technical/passenger): ")
    if service_type == "technical":
        service = TechnicalService()
    elif service_type == "passenger":
        service = PassengerService()
    else:
        raise ValueError("Невідомий тип обслуговування")

    service.perform_service()
