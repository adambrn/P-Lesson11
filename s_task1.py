""" Создайте класс Моя Строка, где: 
будут доступны все возможности str дополнительно хранятся имя автора строки и время создания (time.time) """

import time

class MyString(str):
    """
    Класс MyString, наследуется от встроенного класса str.
    Дополнительно хранит имя автора строки и время создания.
    """
    def __new__(cls, string, author):
        instance = super().__new__(cls, string)
        instance.author = author
        instance.creation_time = time.time()
        return instance

    
if __name__ == "__main__":
    my_string = MyString("Hello, world!", "Adam")
    print(my_string) 
    print(my_string.author) 
    print(my_string.creation_time) 