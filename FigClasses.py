#!/usr/bin/python3

#####=====----- Variables -----=====#####

PI = 3.141592653589793

#####=====----- Classes -----=====#####

class SymFigure():
    base_category = 'Симметричная фигура'
    image = None

class Fig2D():
    class_dimension = 'Плоская фигура'
    def __init__(self):
        pass

class Fig3D():
    class_dimension = 'Объёмная фигура'
    def __init__(self):
        pass

class Circle(SymFigure, Fig2D):
    figure_name = 'Круг'
    def __init__(self):
        super(SymFigure).__init__()
        super(Fig2D).__init__()
    def perimeter(self, r_):
        return 2 * PI * r_
    def square(self, r_):
        return PI * (r_ ** 2)

class Triangle(SymFigure, Fig2D):
    figure_name = 'Равнобедренный треугольник'
    def __init__(self):
        super(SymFigure).__init__()
    def square(self)

class Trapezoid(Fig2D):
    ''' Трапеция
    '''
    def __init__(self):
        super().__init__()

class Rectangle(Fig2D):
    ''' Прямоугольник
    '''
    def __init__(self):
        super().__init__()

class Quadro(Fig2D):
    ''' Квадрат
    '''
    def __init__(self):
        super().__init__()

class Rhombus(Fig2D):
    ''' Ромб
    '''
    def __init__(self):
        super().__init__()

class Sphere(Circle):
    ''' Сфера
    '''
    def __init__(self):
        super(Circle).__init__()
    def square(self, r_):
        return 4 * PI * (r_ ** 2)
    def volume(self, r_):
        return (4 / 3) * PI * (r_ ** 3)

class Cube():
    pass

class Parallelepiped():
    pass

class Pyramid3F():
    pass

class Pyramid4F():
    pass

class Cylinder():
    pass

class Cone():
    pass

#####=====----- Functions -----=====#####

#####=====----- MAIN -----=====#####

if __name__ == '__main__':
    pass

#####=====----- THE END -----=====########################################