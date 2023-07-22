""" Дорабатываем класс прямоугольник из прошлого семинара.
Добавьте возможность сложения и вычитания.
При этом должен создаваться новый экземпляр прямоугольника.
Складываем и вычитаем периметры, а не длинну и ширину.
При вычитании не допускайте отрицательных значений. """

class Rectangle:
    """
    Класс Rectangle, представляет прямоугольник с длиной и шириной.
    Поддерживает операции сложения и вычитания прямоугольников по периметру.
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
        Сложение прямоугольников возвращает квадрат со сложенним периметром
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


if __name__ == "__main__":
    rect1 = Rectangle(4, 3)
    rect2 = Rectangle(5, 2)

    rect_sum = rect1 + rect2
    print(rect_sum.perimeter())

    rect_diff = rect1 - rect2
    print(rect_diff.perimeter())
