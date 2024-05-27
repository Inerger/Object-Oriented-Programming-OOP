# Технічне завдання
Розробити програмне забезпечення для управління залізничною станцією, яке дозволяє керувати поїздами, платформами, розкладами та персоналом.

Декомпонування завдання:

**Моделювання поїздів:**
Визначення атрибутів поїздів (номер, тип, кількість вагонів тощо).
Реалізація фабричного методу для створення різних типів поїздів (пасажирські, вантажні, швидкісні).
Моделювання платформ:

Визначення атрибутів платформ (номер, доступність для різних типів поїздів тощо).
Реалізація абстрактної фабрики для створення різних типів платформ (пасажирські, вантажні).
Моделювання розкладів:

Визначення структури розкладів (час відправлення, час прибуття, платформа, поїзд тощо).
Моделювання персоналу:

Визначення ролей персоналу (машиністи, кондуктори, оператори).
Реалізація фабричного методу для створення різних типів персоналу.
**Використання патернів:**

Фабричний метод (Factory Method):

Використовується для створення об'єктів різних типів поїздів та персоналу.
Абстрактна фабрика (Abstract Factory):

Використовується для створення різних типів платформ, які можуть підтримувати різні типи поїздів.
**Функціональні вимоги:**

Додавання, видалення та редагування інформації про поїзди.
Додавання, видалення та редагування інформації про платформи.
Створення та управління розкладами руху поїздів.
Додавання, видалення та редагування інформації про персонал.
**Технічні вимоги:**

Мова програмування: Python.
Використання патернів проектування для організації коду.
Використання системи контролю версій, наприклад, Git.

#### **Система управління залізничною станцією:**
#### **Лабораторна робота 1 (LW1)**
 #####  - Додавання нових типів потягів (патерн Фабричний метод)
 >Можливі типи потягів:
>> - Швидкісний потяг
>> - Пасажирський потяг
>> - Вантажний потяг
 #### - Вибір способу обслуговування потягів пасажирської категорії (патерн Абстрактна фабрика)
 
 > Типи обслуговування:
>>Технічне обслуговування:
>>> - Періодичний техогляд
>>> - Ремонт

 >>Пасажирське обслуговування:
>>> - Розподіл квитків
>>> - Послуги персоналу потягу

#### **Лабораторна робота 2 (LW1)**
