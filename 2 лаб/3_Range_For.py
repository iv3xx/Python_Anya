def calculate_sum(n):
    S = 0  # Начальная сумма
    for i in range(1, n + 1):
        if i % 2 == 0:  # Проверяем, четное ли число
            S += i  # Если четное, добавляем его
        else:
            S -= i  # Если нечетное, вычитаем его
    return S

n = int(input("Введите значение n: "))
result = calculate_sum(n)
print("Сумма S =", result)
