### Об'єднання операцій обслуговування потягів (Фасад)

# Патерн Фасад
class RefuelService:
    def refuel(self):
        print("Заправка потяга завершена")

class MaintenanceService:
    def perform_maintenance(self):
        print("Технічне обслуговування потяга завершене")

class CleaningService:
    def clean(self):
        print("Очищення вагонів завершено")

class TrainServiceFacade:
    def __init__(self):
        self.refuel_service = RefuelService()
        self.maintenance_service = MaintenanceService()
        self.cleaning_service = CleaningService()

    def service_train(self):
        self.refuel_service.refuel()
        self.maintenance_service.perform_maintenance()
        self.cleaning_service.clean()

# Використання патерну Фасад
if __name__ == "__main__":
    service_facade = TrainServiceFacade()
    service_facade.service_train()

### Захист доступу до управління поїздом (Замісник)

from abc import ABC, abstractmethod

# Патерн Замісник
class TrainController(ABC):
    @abstractmethod
    def depart(self):
        pass

    @abstractmethod
    def arrive(self):
        pass

class RealTrainController(TrainController):
    def depart(self):
        print("Потяг відправляється")

    def arrive(self):
        print("Потяг прибуває")

class ProxyTrainController(TrainController):
    def __init__(self, real_controller: RealTrainController, user_role: str):
        self.real_controller = real_controller
        self.user_role = user_role

    def depart(self):
        if self.user_role == "admin":
            self.real_controller.depart()
        else:
            print("Відмовлено у доступі: недостатньо прав")

    def arrive(self):
        if self.user_role == "admin":
            self.real_controller.arrive()
        else:
            print("Відмовлено у доступі: недостатньо прав")

# Використання патерну Замісник
if __name__ == "__main__":
    real_controller = RealTrainController()
    proxy_controller = ProxyTrainController(real_controller, user_role="user")
    proxy_controller.depart()
    proxy_controller.arrive()
    
    proxy_controller_admin = ProxyTrainController(real_controller, user_role="admin")
    proxy_controller_admin.depart()
    proxy_controller_admin.arrive()

### Розподіл способів обробки даних потягів і типів інтерфейсів (Міст)

from abc import ABC, abstractmethod

# Патерн Міст: Обробка даних
class TrainDataProcessor(ABC):
    @abstractmethod
    def process_data(self):
        pass

class RealDataProcessor(TrainDataProcessor):
    def process_data(self):
        print("Реальна обробка даних потяга")

class SimulatedDataProcessor(TrainDataProcessor):
    def process_data(self):
        print("Імітаційна обробка даних потяга")

# Патерн Міст: Типи інтерфейсів
class TrainInterface(ABC):
    def __init__(self, data_processor: TrainDataProcessor):
        self.data_processor = data_processor

    @abstractmethod
    def display(self):
        pass

class GraphicalInterface(TrainInterface):
    def display(self):
        print("Графічний інтерфейс:")
        self.data_processor.process_data()

class ConsoleInterface(TrainInterface):
    def display(self):
        print("Консольний інтерфейс:")
        self.data_processor.process_data()

# Використання патерну Міст
if __name__ == "__main__":
    real_processor = RealDataProcessor()
    simulated_processor = SimulatedDataProcessor()

    graphical_interface = GraphicalInterface(real_processor)
    console_interface = ConsoleInterface(simulated_processor)

    graphical_interface.display()
    console_interface.display()