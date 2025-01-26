class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        self.__commands = []

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def add_command(self, command):
        self.__commands.append(command)

    def get_commands(self):
        return self.__commands

    def make_sound(self):
        raise NotImplementedError("Subclasses must implement this method")


class Dog(Animal):
    def make_sound(self):
        return "Woof!"


class Cat(Animal):
    def make_sound(self):
        return "Meow!"


class AnimalRegistry:
    def __init__(self):
        self.animals = []

    def add_animal(self):
        name = input("Введите имя животного: ")
        age = int(input("Введите возраст животного: "))
        animal_type = input("Введите тип животного (собака/кошка): ").lower()

        if animal_type == "собака":
            animal = Dog(name, age)
        elif animal_type == "кошка":
            animal = Cat(name, age)
        else:
            print("Некорректный тип животного.")
            return

        self.animals.append(animal)
        print(f"{animal.get_name()} был добавлен в реестр!")

    def list_commands(self):
        name = input("Введите имя животного для просмотра команд: ")
        animal = self.find_animal(name)

        if animal:
            commands = animal.get_commands()
            if commands:
                print(f"Команды для {animal.get_name()}: {', '.join(commands)}")
            else:
                print(f"{animal.get_name()} еще не обучен ни одной команде.")
        else:
            print("Животное не найдено.")

    def train_animal(self):
        name = input("Введите имя животного для обучения: ")
        animal = self.find_animal(name)

        if animal:
            command = input("Введите команду для обучения: ")
            animal.add_command(command)
            print(f"{animal.get_name()} теперь знает команду '{command}'!")
        else:
            print("Животное не найдено.")

    def find_animal(self, name):
        for animal in self.animals:
            if animal.get_name().lower() == name.lower():
                return animal
        return None

    def display_menu(self):
        while True:
            print("\n--- Реестр домашних животных ---")
            print("1. Завести новое животное")
            print("2. Посмотреть список команд животного")
            print("3. Обучить животное новой команде")
            print("4. Выход")
            choice = input("Выберите опцию: ")

            if choice == "1":
                self.add_animal()
            elif choice == "2":
                self.list_commands()
            elif choice == "3":
                self.train_animal()
            elif choice == "4":
                print("Выход из программы.")
                break
            else:
                print("Некорректный выбор! Пожалуйста, выберите снова.")


if __name__ == "__main__":
    registry = AnimalRegistry()
    registry.display_menu()