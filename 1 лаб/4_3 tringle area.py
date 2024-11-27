import math

def calculate_triangle_area():
    # Ввод сторон и угла
    a = float(input("Введите длину первой стороны (a): "))
    b = float(input("Введите длину второй стороны (b): "))
    angle_degrees = float(input("Введите угол между ними в градусах: "))

    # Преобразуем угол в радианы
    angle_radians = math.radians(angle_degrees)

    # Вычисляем площадь
    area = 0.5 * a * b * math.sin(angle_radians)

    # Выводим результат
    print("Площадь треугольника:", area)

calculate_triangle_area()
