def calculate_y(x, z):
    # Вычисление вспомогательных переменных
    x_squared = x ** 2
    z_squared = z ** 2
    term1 = 5 * x ** 4 + 20 * x_squared
    term2 = z_squared + 3
    absolute_term = abs(term1 / term2)
    additional_term = (x_squared + 1) ** 3

    # Полное выражение
    y = x_squared + 4 * z - absolute_term + additional_term
    return y

# Тестовые примеры
test_cases = [
    (1, 2),
    (2, 1),
    (0, 3),
    (-1, 4),
    (3, 0)
]

# Вывод результатов тестов
for x, z in test_cases:
    result = calculate_y(x, z)
    print(f"y({x}, {z}) = {result}")

