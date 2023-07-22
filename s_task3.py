# Доработаем класс Архив из задачи 2.
# Добавьте методы представления экземпляра для программиста и для пользователя.

class Archive:
    """
    Класс Archive, хранит пару свойств - число и строку.
    При создании нового экземпляра класса, сохраняет старые данные в пару списков-архивов.
    Списки-архивы также являются свойствами экземпляра.
    """
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.number_archive = []
            cls._instance.string_archive = []
        else:
            cls._instance.number_archive.append(cls._instance.number)
            cls._instance.string_archive.append(cls._instance.string)
        return cls._instance
            

    def __init__(self, number, string):
        self.number = number
        self.string = string
        
    def __repr__(self):
        return f"Archive(number={self.number}, string='{self.string}')"

    def __str__(self):
        return f"Number: {self.number}, String: {self.string}, Number archive: {self.number_archive}, String archive: {self.string_archive}"

if __name__ == "__main__":
    obj1 = Archive(42, "world")
    
    print(obj1)
    print(repr(obj1))  
    
    obj2 = Archive(73, "hello")

    print(obj2)
    print(repr(obj2))
    

    obj3 = Archive(22, "!")

    print(obj3)
    print(repr(obj3))

