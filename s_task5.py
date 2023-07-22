# Доработайте прошлую задачу.
# Добавьте сравнение прямоугольников по площади
# Должны работать все шесть операций сравнения

class Rectangle:
    """
    Класс Rectangle, представляет прямоугольник с длиной и шириной.
    Поддерживает операции сложения и вычитания прямоугольников, а также сравнение по площади.
    """
    def __init__(self, length, width=None):
        self.length = length
        self.width = length if width is None else width

    def perimeter(self):
        """
        Периметр прямоугольника
        """
        return 2 * (self.length + self.width)

    def area(self):
        """
        Площадь прямоугольника
        """
        return self.length * self.width

    def __add__(self, other):
        """
        Сложение прямоугольников возвращает квадрат со сложенным периметром
        """
        total_perimeter = self.perimeter() + other.perimeter()
        return Rectangle(total_perimeter // 4)

    def __sub__(self, other):
        """
        Вычетание прямоугольников возвращает квадрат с разностью периметров
        если разность отрицательная - нулевой
        """
        result_perimeter = self.perimeter() - other.perimeter()
        new_perimeter = max(0, result_perimeter)
        return Rectangle(new_perimeter // 4)
    
    def __eq__(self, other):
        return self.area() == other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

if __name__ == "__main__":
    rect1 = Rectangle(4, 3)
    rect2 = Rectangle(5, 2)

    print(rect1 == rect2)  
    print(rect1 != rect2)  
    print(rect1 < rect2)   
    print(rect1 <= rect2)  
    print(rect1 > rect2)   
    print(rect1 >= rect2)  
