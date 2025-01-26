class Counter:
    def __init__(self):
        self.count = 0
        self.is_opened = False

    def add(self):
        if not self.is_opened:
            raise Exception("Счетчик не открыт для работы.")
        self.count += 1

    def __enter__(self):
        self.is_opened = True
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if not self.is_opened:
            raise Exception("Счетчик был закрыт и не был использован в контексте.") 
        self.is_opened = False

    def get_count(self):
        return self.count


# Пример использования класса Counter
class AnimalRegistry:
    def __init__(self):
        self.animals = []

    def add_animal(self, name, age):
        if not name or age <= 0:
            print("Ошибка: заполняйте все поля.")
            return False
        self.animals.append({"name": name, "age": age})
        return True


# Основная программа
if __name__ == "__main__":
    registry = AnimalRegistry()

    with Counter() as counter:
        while True:
            name = input("Введите имя животного или 'exit' для выхода: ")
            if name.lower() == 'exit':
                break
            age = input("Введите возраст животного (положительное число): ")
            try:
                age = int(age)
            except ValueError:
                print("Возраст должен быть числом.")
                continue
            
            if registry.add_animal(name, age):
                counter.add()
                print(f"Добавлено новое животное: {name}.")
                print(f"Общее количество животных: {counter.get_count()}.")