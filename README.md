# Object-Oriented-Programming-OOP

*Технічне завдання*

## Система управління залізничною станцією

# Абстрактний клас або інтерфейс "Номер"
class Room:
    def display_info(self):
        pass

# Конкретний клас для стандартного номера
class StandardRoom(Room):
    def display_info(self):
        print("This is a standard room.")

# Конкретний клас для люксового номера
class LuxuryRoom(Room):
    def display_info(self):
        print("This is a luxury room.")

# Фабричний метод
class RoomFactory:
    def create_room(self, room_type):
        if room_type == "standard":
            return StandardRoom()
        elif room_type == "luxury":
            return LuxuryRoom()
        else:
            return None

# Приклад використання
factory = RoomFactory()
room1 = factory.create_room("standard")
room1.display_info()  # Output: This is a standard room.

room2 = factory.create_room("luxury")
room2.display_info()  # Output: This is a luxury room.
