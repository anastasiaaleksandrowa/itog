class Animal:
    def __init__(self, name, age):
        self.__name = name  # Инкапсуляция: защищаем имя животного
        self.__age = age    # Инкапсуляция: защищаем возраст животного
        
    def get_name(self):
        return self.__name  # Метод для доступа к имени
    
    def get_age(self):
        return self.__age    # Метод для доступа к возрасту
    
    def make_sound(self):
        raise NotImplementedError("Subclasses must implement this method")  # Абстрактный метод


class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)  # Вызов конструктора базового класса
        self.__breed = breed  # Инкапсуляция: защищаем породу собаки
        
    def get_breed(self):
        return self.__breed  # Метод для доступа к породе

    def make_sound(self):
        return "Woof!"  # Реализация метода для собаки


class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)  # Вызов конструктора базового класса
        self.__color = color  # Инкапсуляция: защищаем цвет кошки
        
    def get_color(self):
        return self.__color  # Метод для доступа к цвету

    def make_sound(self):
        return "Meow!"  # Реализация метода для кошки


# Пример использования классов
dog = Dog("Buddy", 3, "Golden Retriever")
cat = Cat("Whiskers", 2, "Gray")

print(f"{dog.get_name()} is a {dog.get_breed()} and says {dog.make_sound()}.")
print(f"{cat.get_name()} is a {cat.get_color()} cat and says {cat.make_sound()}.")