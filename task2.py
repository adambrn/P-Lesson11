#Создайте класс Матрица. Добавьте методы для: вывода на печать, проверку на равенство, сложения, *умножения матриц

class Matrix:
    """
    Класс Матрица представляет двумерный массив.
    Поддерживает методы вывода на печать, проверки на равенство, сложения и умножения матриц.
    """
    def __init__(self, matrix):
        """
        matrix (list): Двумерный массив - матрица.
        """
        self.matrix = matrix

    def __str__(self):
        return "\n".join(" ".join(str(element) for element in row) for row in self.matrix)

    def __eq__(self, other):
        """
        Сравнивает матрицы на равенство.
        """
        return self.matrix == other.matrix

    def __add__(self, other):
        """
        Возвращает новую матрицу - результат сложения с другой матрицей.
        """
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            raise ValueError("Матрицы разных размеров нельзя сложить.")
        
        result_matrix = []
        for i in range(len(self.matrix)):
            row = []
            for j in range(len(self.matrix[0])):
                row.append(self.matrix[i][j] + other.matrix[i][j])
            result_matrix.append(row)
        
        return Matrix(result_matrix)

    def __mul__(self, other):
        """
        Возвращает новую матрицу - результат умножения с другой матрицей.
        """
        if len(self.matrix[0]) != len(other.matrix):
            raise ValueError("Число столбцов первой матрицы должно быть равно числу строк второй матрицы.")

        result_matrix = []
        for i in range(len(self.matrix)):
            row = []
            for j in range(len(other.matrix[0])):
                element = sum(self.matrix[i][k] * other.matrix[k][j] for k in range(len(self.matrix[0])))
                row.append(element)
            result_matrix.append(row)

        return Matrix(result_matrix)

if __name__ == "__main__":
    matrix1 = Matrix([[1, 2], [3, 4]])
    matrix2 = Matrix([[5, 6], [7, 8]])
    matrix3 = Matrix([[1, 2], [3, 4]])

    print(matrix1)  

    print(matrix1 == matrix2)  
    print(matrix1 == matrix3)  
    
    matrix_sum = matrix1 + matrix2
    print(matrix_sum)  
    

    matrix_mult = matrix1 * matrix2
    print(matrix_mult)  

    help(Matrix)
    
