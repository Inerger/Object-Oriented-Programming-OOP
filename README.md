#### Технічне завдання
Розробити програмне забезпечення для управління залізничною станцією, яке дозволяє керувати поїздами, платформами, розкладами та персоналом 
(Система управління залізничною станцією).

**Функціональні вимоги:**
Додавання, видалення та редагування інформації про поїзди.
Додавання, видалення та редагування інформації про платформи.
Створення та управління розкладами руху поїздів.
Додавання, видалення та редагування інформації про персонал.

**Технічні вимоги:**
Мова програмування: Python.
Використання патернів проектування для організації коду.
Використання системи контролю версій Git.

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

#### Декомпонування завдання:

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

#### Фабричний метод (Factory Method):

Використовується для створення об'єктів різних типів поїздів та персоналу.
Абстрактна фабрика (Abstract Factory):
Використовується для створення різних типів платформ, які можуть підтримувати різні типи поїздів.

#### **Лабораторна робота 2 (LW2)**

##### - Реалізація типів вагонів (патерн Прототип)
> Можливі типи вагонів:
>> - Купейний вагон
>> - Плацкартний вагон
>> - Вагон-ресторан

##### - Створення складних конфігурацій поїздів (патерн Будівельник)
> Можливі конфігурації:
>> - Швидкісний потяг
>> - Пасажирський потяг
>> - Вантажний потяг

#### Декомпонування завдання

1. **Реалізація типів вагонів (Прототип)**
    - **Завдання:**
        - Створити абстрактний клас `Wagon` з методом `clone()`.
        - Реалізувати класи для кожного типу вагона: `CoupeWagon`, `PlatzkartWagon`, `RestaurantWagon`.
        - Реалізувати метод `clone()` для кожного типу вагона.

2. **Створення складних конфігурацій поїздів (Будівельник)**
    - **Завдання:**
        - Створити абстрактний клас `TrainBuilder` з методами для додавання вагонів та отримання поїзда.
        - Реалізувати конкретні класи-будівельники для кожної конфігурації поїздів: `HighSpeedTrainBuilder`, `PassengerTrainBuilder`, `FreightTrainBuilder`.
        - Створити клас `Train` для представлення поїзда.
        - Створити клас `Director` для керування процесом будівництва поїздів.

У цьому коді:

1. **Патерн Прототип** реалізує можливість створення копій вагонів. Кожен тип вагона (`CoupeWagon`, `PlatzkartWagon`, `RestaurantWagon`) має метод `clone()`, який створює глибоку копію об'єкта.

2. **Патерн Будівельник** реалізує створення складних конфігурацій поїздів. Абстрактний клас `TrainBuilder` визначає інтерфейс для будівельників поїздів, а конкретні класи-будівельники (`HighSpeedTrainBuilder`, `PassengerTrainBuilder`, `FreightTrainBuilder`) реалізують цей інтерфейс для створення різних конфігурацій поїздів. Клас `Director` керує процесом будівництва поїзда, використовуючи відповідного будівельника.

#### Лабораторна робота 3 (LW3)

##### **1. Вибір стратегії обслуговування потягів (патерн Стратегія)**
> **Типи стратегій обслуговування:**
>> - Технічне обслуговування
>> - Обслуговування пасажирів
>> - Обслуговування вантажу

##### **2. Реалізація системи оповіщення диспетчерів про статус потягів (патерн Спостерігач)**
> **Події для оповіщення:**
>> - Прибуття потяга
>> - Відправлення потяга
>> - Затримка потяга

##### **3. Виконання команд для управління станцією (патерн Команда)**
> **Типи команд:**
>> - Прибуття потяга на станцію
>> - Відправлення потяга зі станції
>> - Зміна колії

#### Декомпонування завдання

1. **Вибір стратегії обслуговування потягів (Стратегія)**
    - **Завдання:**
        - Створити інтерфейс `ServiceStrategy` з методом `execute_service()`.
        - Реалізувати класи для кожної стратегії обслуговування: `TechnicalService`, `PassengerService`, `CargoService`.
        - Додати можливість вибору стратегії обслуговування для потягів.

2. **Реалізація системи оповіщення диспетчерів про статус потягів (Спостерігач)**
    - **Завдання:**
        - Створити інтерфейс `Observer` з методом `update()`.
        - Створити клас `TrainStatusNotifier`, який реалізує додавання, видалення і сповіщення спостерігачів.
        - Реалізувати класи спостерігачів, які будуть реагувати на події: `ArrivalObserver`, `DepartureObserver`, `DelayObserver`.

3. **Виконання команд для управління станцією (Команда)**
    - **Завдання:**
        - Створити інтерфейс `Command` з методом `execute()`.
        - Реалізувати класи команд: `TrainArrivalCommand`, `TrainDepartureCommand`, `ChangeTrackCommand`.
        - Створити клас `StationController` для виконання команд.

1. **Стратегія (Strategy)**: Патерн використовується для вибору стратегії обслуговування потягів. Створюються конкретні стратегії для технічного обслуговування, обслуговування пасажирів та обслуговування вантажу. Клас `Train` використовує ці стратегії для виконання обслуговування.

2. **Спостерігач (Observer)**: Патерн використовується для реалізації системи оповіщення диспетчерів про статус потягів. Клас `TrainStatusNotifier` відповідає за управління спостерігачами та сповіщення їх про події (прибуття, відправлення, затримка потяга). Класи спостерігачів (`ArrivalObserver`, `DepartureObserver`, `DelayObserver`) реагують на ці події.

3. **Команда (Command)**: Патерн використовується для виконання команд для управління станцією. Створюються конкретні команди для прибуття потяга, відправлення потяга та зміни колії. Клас `StationController` відповідає за додавання та виконання команд.

#### Лабораторна робота 4 (LW4)

##### **1. Виконання макрокоманд для комплексних операцій (патерн Макрокоманди)**
> **Приклади макрокоманд:**
>> - Операція прибуття потяга (включає зміну колії, повідомлення диспетчера, перевірку вагонів)
>> - Операція відправлення потяга (включає оголошення, перевірку стану потяга, випуск потяга на колію)

##### **2. Реалізація процесу обслуговування потяга (патерн Шаблонний метод)**
> **Приклади процесів:**
>> - Процес технічного обслуговування
>> - Процес пасажирського обслуговування

#### Декомпонування завдання

1. **Виконання макрокоманд для комплексних операцій (Макрокоманди)**
    - **Завдання:**
        - Створити інтерфейс `Command` з методом `execute()`.
        - Реалізувати класи для окремих команд: `ChangeTrackCommand`, `NotifyDispatcherCommand`, `CheckWagonsCommand`, `AnnounceDepartureCommand`, `CheckTrainStatusCommand`, `ReleaseTrainCommand`.
        - Створити класи макрокоманд: `TrainArrivalMacroCommand`, `TrainDepartureMacroCommand`.

2. **Реалізація процесу обслуговування потяга (Шаблонний метод)**
    - **Завдання:**
        - Створити абстрактний клас `TrainService` з шаблонним методом `perform_service()`.
        - Реалізувати методи в класі `TrainService`, які можуть бути перевизначені в підкласах.
        - Реалізувати класи `TechnicalService` і `PassengerService`, які наслідують `TrainService` і перевизначають необхідні методи.

#### Пояснення:

1. **Макрокоманди**: Патерн використовується для створення комплексних операцій, що складаються з кількох команд. В даному випадку, макрокоманди `TrainArrivalMacroCommand` і `TrainDepartureMacroCommand` об'єднують окремі команди (`ChangeTrackCommand`, `NotifyDispatcherCommand`, `CheckWagonsCommand`, `AnnounceDepartureCommand`, `CheckTrainStatusCommand`, `ReleaseTrainCommand`) для виконання складних операцій.

2. **Шаблонний метод (Template Method)**: Патерн використовується для визначення скелету алгоритму в методі базового класу, делегуючи реалізацію конкретних кроків підкласам. В даному випадку, шаблонний метод `perform_service()` в класі `TrainService` визначає загальні кроки обслуговування потяга, а конкретні реалізації цих кроків (`perform_specific_service()`) визначаються в підкласах `TechnicalService` і `PassengerService`.


#### Лабораторна робота 5 (LW5)

##### **1. Перегляд списку потягів на станції (патерн Ітератор)**
> **Завдання:**
>> - Створити структуру, що представляє список потягів.
>> - Реалізувати ітератор для проходження по списку потягів.

##### **2. Управління станом потяга (патерн Стан)**
> **Завдання:**
>> - Реалізувати класи, що представляють різні стани потяга (прибув, обслуговується, готовий до відправлення).
>> - Забезпечити зміну станів потяга в залежності від виконаних операцій.

##### **3. Обробка запитів на обслуговування потяга (патерн Ланцюжок Обов'язків)**
> **Завдання:**
>> - Реалізувати ланцюжок обробників запитів на обслуговування (початковий огляд, технічне обслуговування, перевірка документів).
>> - Забезпечити можливість обробки запиту через ланцюжок обов'язків.

#### Декомпонування завдання

1. **Перегляд списку потягів на станції (Ітератор)**
    - **Завдання:**
        - Створити клас `Train` для представлення потяга.
        - Створити клас `TrainCollection` для зберігання списку потягів.
        - Реалізувати клас `TrainIterator` для ітерації по списку потягів.

2. **Управління станом потяга (Стан)**
    - **Завдання:**
        - Створити абстрактний клас `TrainState` з методами для зміни станів.
        - Реалізувати класи станів: `ArrivedState`, `ServicingState`, `ReadyToDepartState`.
        - Реалізувати методи для переходу між станами.

3. **Обробка запитів на обслуговування потяга (Ланцюжок Обов'язків)**
    - **Завдання:**
        - Створити інтерфейс `RequestHandler` з методом `handle_request()`.
        - Реалізувати класи обробників: `InitialInspectionHandler`, `TechnicalServiceHandler`, `DocumentCheckHandler`.
        - Зв'язати обробники в ланцюжок для послідовної обробки запитів.

#### Пояснення:

1. **Ітератор**: Патерн використовується для надання послідовного доступу до елементів колекції без розкриття її внутрішнього представлення. У прикладі створено ітератор для перегляду списку потягів на станції.

2. **Стан**: Патерн використовується для зміни поведінки об'єкта при зміні його внутрішнього стану. У прикладі створено різні стани потяга (прибув, обслуговується, готовий до відправлення) та методи для переходу між цими станами.

3. **Ланцюжок Обов'язків**: Патерн використовується для передачі запитів вздовж ланцюжка обробників. У прикладі створено ланцюжок обробників для обробки запитів на обслуговування потяга (початковий огляд, технічне обслуговування, перевірка документів).

#### Лабораторна робота 6 (LW6)

##### **1. Парсинг та виконання команд на станції (патерн Інтерпретатор)**
> **Завдання:**
>> - Реалізувати інтерпретатор для команд на залізничній станції (наприклад, зміна колії, прибуття/відправлення потяга).
>> - Забезпечити можливість додавання нових команд без зміни існуючого коду.

##### **2. Координація взаємодії між об'єктами станції (патерн Посередник)**
> **Завдання:**
>> - Реалізувати посередника для управління взаємодією між об'єктами на станції (наприклад, диспетчери, потяги, платформи).
>> - Забезпечити централізоване управління та комунікацію між об'єктами через посередника.

#### Декомпонування завдання

1. **Парсинг та виконання команд на станції (Інтерпретатор)**
    - **Завдання:**
        - Створити інтерфейс `Expression` з методом `interpret()`.
        - Реалізувати класи для різних команд: `ChangeTrackCommand`, `ArrivalCommand`, `DepartureCommand`.
        - Реалізувати клас `CommandInterpreter`, який буде парсити та виконувати команди.

2. **Координація взаємодії між об'єктами станції (Посередник)**
    - **Завдання:**
        - Створити інтерфейс `Mediator` з методами для реєстрації об'єктів та обробки повідомлень.
        - Реалізувати клас `StationMediator`, який буде керувати взаємодією між об'єктами.
        - Створити класи для об'єктів, що взаємодіють через посередника: `Dispatcher`, `Train`, `Platform`.

#### Пояснення:

1. **Інтерпретатор**: Патерн використовується для створення інтерпретатора команд на залізничній станції. У прикладі реалізовано інтерфейс `Expression` та класи команд `ChangeTrackCommand`, `ArrivalCommand`, `DepartureCommand`. Клас `CommandInterpreter` інтерпретує вхідні команди та повертає відповідний об'єкт команди.

2. **Посередник**: Патерн використовується для координації взаємодії між об'єктами станції. У прикладі реалізовано інтерфейс `Mediator` та клас `StationMediator`, який керує взаємодією між об'єктами `Dispatcher`, `Train` та `Platform`. Об'єкти взаємодіють між собою через посередника, що забезпечує централізоване управління повідомленнями та подіями.

#### Лабораторна робота 7 (LW7)

##### **1. Збереження стану потяга (патерн Зберігач)**
> **Завдання:**
>> - Реалізувати можливість збереження та відновлення стану потяга.
>> - Забезпечити функціональність для створення знімків стану потяга та їх відновлення при необхідності.

##### **2. Відвідування різних елементів станції (патерн Відвідувач)**
> **Завдання:**
>> - Реалізувати можливість виконання операцій над різними елементами станції (потягами, платформами, диспетчерами) без зміни їх класів.
>> - Забезпечити можливість додавання нових операцій без зміни існуючих класів елементів.

#### Декомпонування завдання

1. **Збереження стану потяга (Зберігач)**
    - **Завдання:**
        - Створити клас `TrainState` для представлення стану потяга.
        - Реалізувати клас `Train` з методами для створення та відновлення знімків стану.
        - Створити клас `TrainMemento` для зберігання знімків стану потяга.
        - Реалізувати клас `TrainCaretaker` для управління збереженими знімками.

2. **Відвідування різних елементів станції (Відвідувач)**
    - **Завдання:**
        - Створити інтерфейс `Element` з методом `accept(visitor)`.
        - Реалізувати класи елементів станції (`Train`, `Platform`, `Dispatcher`), що реалізують інтерфейс `Element`.
        - Створити інтерфейс `Visitor` з методами для відвідування кожного типу елементів.
        - Реалізувати класи відвідувачів для виконання конкретних операцій над елементами.

#### Пояснення:

1. **Зберігач**: Патерн використовується для збереження та відновлення стану об'єкта без порушення інкапсуляції. У прикладі реалізовано класи `TrainState`, `TrainMemento`, `Train`, та `TrainCaretaker` для збереження та відновлення стану потяга.

2. **Відвідувач**: Патерн використовується для виконання операцій над елементами об'єкта без зміни їх класів. У прикладі реалізовано інтерфейс `Visitor` та класи елементів `Train`, `Platform`, `Dispatcher`, що реалізують інтерфейс `Element`. Клас `StatusVisitor` реалізує методи для відвідування кожного типу елементів і виконання операцій над ними.

#### Класи та їх функції:
- **TrainState**: Зберігає інформацію про стан потяга, наприклад, його позицію та статус.
- **TrainMemento**: Клас-зберігач, який зберігає знімок стану потяга.
- **Train**: Основний клас потяга, який має методи для зміни стану, збереження стану в знімок (memento) та відновлення стану з знімка.
- **TrainCaretaker**: Клас, який управляє збереженими знімками стану потяга.
- **Visitor**: Інтерфейс, який визначає методи для відвідування кожного типу елементів.
- **Element**: Інтерфейс, який визначає метод `accept(visitor)`, що приймає відвідувача.
- **Train, Platform, Dispatcher**: Класи, що реалізують інтерфейс `Element` і представляють різні елементи станції.
- **StatusVisitor**: Клас відвідувача, який реалізує методи для виконання операцій над кожним типом елементів.

#### Лабораторна робота 8 (LW8)

