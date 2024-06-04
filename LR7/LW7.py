### Збереження стану потяга (Зберігач)
# Патерн Зберігач
class TrainState:
    def __init__(self, position: str, status: str):
        self.position = position
        self.status = status

class TrainMemento:
    def __init__(self, state: TrainState):
        self._state = state

    def get_state(self) -> TrainState:
        return self._state

class Train:
    def __init__(self, position: str, status: str):
        self._state = TrainState(position, status)

    def change_state(self, position: str, status: str):
        self._state = TrainState(position, status)

    def save_state(self) -> TrainMemento:
        return TrainMemento(self._state)

    def restore_state(self, memento: TrainMemento):
        self._state = memento.get_state()

    def __str__(self):
        return f"Потяг в позиції {self._state.position} зі статусом {self._state.status}"

class TrainCaretaker:
    def __init__(self):
        self._mementos = []

    def add_memento(self, memento: TrainMemento):
        self._mementos.append(memento)

    def get_memento(self, index: int) -> TrainMemento:
        return self._mementos[index]

# Використання зберігача
if __name__ == "__main__":
    train = Train("Колія 1", "Прибуття")
    caretaker = TrainCaretaker()

    # Збереження стану потяга
    caretaker.add_memento(train.save_state())

    # Зміна стану потяга
    train.change_state("Колія 2", "Обслуговування")
    print(train)

    # Відновлення попереднього стану потяга
    train.restore_state(caretaker.get_memento(0))
    print(train)

### Відвідування різних елементів станції (Відвідувач)

from abc import ABC, abstractmethod

# Патерн Відвідувач
class Visitor(ABC):
    @abstractmethod
    def visit_train(self, train):
        pass

    @abstractmethod
    def visit_platform(self, platform):
        pass

    @abstractmethod
    def visit_dispatcher(self, dispatcher):
        pass

class Element(ABC):
    @abstractmethod
    def accept(self, visitor: Visitor):
        pass

class Train(Element):
    def __init__(self, name: str):
        self.name = name

    def accept(self, visitor: Visitor):
        visitor.visit_train(self)

class Platform(Element):
    def __init__(self, number: int):
        self.number = number

    def accept(self, visitor: Visitor):
        visitor.visit_platform(self)

class Dispatcher(Element):
    def __init__(self, name: str):
        self.name = name

    def accept(self, visitor: Visitor):
        visitor.visit_dispatcher(self)

class StatusVisitor(Visitor):
    def visit_train(self, train: Train):
        print(f"Відвідувач перевіряє потяг: {train.name}")

    def visit_platform(self, platform: Platform):
        print(f"Відвідувач перевіряє платформу: {platform.number}")

    def visit_dispatcher(self, dispatcher: Dispatcher):
        print(f"Відвідувач перевіряє диспетчера: {dispatcher.name}")

# Використання відвідувача
if __name__ == "__main__":
    elements = [
        Train("Швидкісний потяг"),
        Platform(1),
        Dispatcher("Диспетчер Іван")
    ]

    visitor = StatusVisitor()

    for element in elements:
        element.accept(visitor)
