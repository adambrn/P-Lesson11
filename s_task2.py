# Создайте класс Архив, который хранит пару свойств. Например, число и строку.
# При нового экземпляра класса, старые данные из ранее созданных экземпляров сохраняются в пару списков-архивов
# list-архивы также являются свойствами экземпляра

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
        
  
    def __str__(self) -> str:
        return f"{self.number} {self.string}"

if __name__ == "__main__":
    obj1 = Archive(42, "world")
    
    print(obj1)
    print(obj1.number_archive)  
    print(obj1.string_archive)  
    
    obj2 = Archive(73, "hello")

    print(obj2)
    print(obj2.number_archive)  
    print(obj2.string_archive) 

    obj3 = Archive(22, "!")

    print(obj3)
    print(obj3.number_archive)  
    print(obj3.string_archive) 
