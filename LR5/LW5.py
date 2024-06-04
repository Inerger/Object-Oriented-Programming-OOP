###Перегляд списку потягів на станції (Ітератор)

from typing import List, Iterator

class Train:
    def __init__(self, name: str):
        self.name = name

class TrainCollection:
    def __init__(self):
        self._trains: List[Train] = []

    def add_train(self, train: Train):
        self._trains.append(train)

    def __iter__(self) -> Iterator[Train]:
        return iter(self._trains)

# Використання ітератора
if __name__ == "__main__":
    collection = TrainCollection()
    collection.add_train(Train("Швидкісний потяг"))
    collection.add_train(Train("Пасажирський потяг"))
    collection.add_train(Train("Вантажний потяг"))

    for train in collection:
        print(f"Потяг: {train.name}")


###Управління станом потяга (Стан)

from abc import ABC, abstractmethod

class TrainContext:
    def __init__(self, state):
        self.state = state

    def change_state(self, state):
        self.state = state

    def request(self):
        self.state.handle(self)

class TrainState(ABC):
    @abstractmethod
    def handle(self, context: TrainContext):
        pass

class ArrivedState(TrainState):
    def handle(self, context: TrainContext):
        print("Потяг прибув на станцію.")
        context.change_state(ServicingState())

class ServicingState(TrainState):
    def handle(self, context: TrainContext):
        print("Потяг обслуговується.")
        context.change_state(ReadyToDepartState())

class ReadyToDepartState(TrainState):
    def handle(self, context: TrainContext):
        print("Потяг готовий до відправлення.")
        context.change_state(ArrivedState())  # Для прикладу змінюємо назад до прибуття

# Використання станів
if __name__ == "__main__":
    train = TrainContext(ArrivedState())
    train.request()  # Потяг прибув на станцію.
    train.request()  # Потяг обслуговується.
    train.request()  # Потяг готовий до відправлення.


###Обробка запитів на обслуговування потяга (Ланцюжок Обов'язків)

from abc import ABC, abstractmethod

class RequestHandler(ABC):
    def __init__(self):
        self.next_handler = None

    def set_next(self, handler):
        self.next_handler = handler
        return handler

    @abstractmethod
    def handle_request(self, request):
        if self.next_handler:
            self.next_handler.handle_request(request)

class InitialInspectionHandler(RequestHandler):
    def handle_request(self, request):
        if request == "initial_inspection":
            print("Проведення початкового огляду потяга.")
        else:
            super().handle_request(request)

class TechnicalServiceHandler(RequestHandler):
    def handle_request(self, request):
        if request == "technical_service":
            print("Проведення технічного обслуговування потяга.")
        else:
            super().handle_request(request)

class DocumentCheckHandler(RequestHandler):
    def handle_request(self, request):
        if request == "document_check":
            print("Перевірка документів потяга.")
        else:
            super().handle_request(request)

# Використання ланцюжка обов'язків
if __name__ == "__main__":
    initial_inspection = InitialInspectionHandler()
    technical_service = initial_inspection.set_next(TechnicalServiceHandler())
    document_check = technical_service.set_next(DocumentCheckHandler())

    # Відправка запитів на обробку
    initial_inspection.handle_request("initial_inspection")
    initial_inspection.handle_request("technical_service")
    initial_inspection.handle_request("document_check")
    initial_inspection.handle_request("unknown_request")  # Необроблений запит