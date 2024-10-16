def area(a, h):
    '''Возвращает площадь треугольника со стороной a и высотой h
                Параметры:
                    a: сторона треугольника
                    h: высота треугольника
                Возвращаемое значение:
                    a * a: площадь треугольника
                Пример вызова area(3, 2):
                    Входные данные: 3, 2
                    Вывод: 3'''
    return a * h / 2
    

def perimeter(a, b, c):
    '''Возвращает периметр треугольника со сторонами a, b и c 
        Параметры:
            a, b, c: стороны треугольника
            h: высота треугольника
        Возвращаемое значение:
            a + b + c: периметр треугольника
        Пример вызова perimetr(3, 2, 1):
            Входные данные: 3 2 1
            Вывод: 6'''
    return a + b + c 