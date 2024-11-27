import math

def compute_z1(b):
    """Вычисляет z1 = (√(2b + 2√(b^2 - 4)) / √(b^2 - 4 + b + 2))"""
    # Проверяем, чтобы под корнем не было отрицательных значений
    if b**2 < 4:
        raise ValueError("b^2 must be greater than or equal to 4 for real results.")
    
    numerator = math.sqrt(2 * b + 2 * math.sqrt(b**2 - 4))
    denominator = math.sqrt(b**2 - 4 + b + 2)
    return numerator / denominator

def compute_z2(b):
    """Вычисляет z2 = (1 / √(b + 2))"""
    if b + 2 <= 0:
        raise ValueError("b + 2 must be greater than 0 for real results.")
    
    return 1 / math.sqrt(b + 2)

# Пример использования функций
b_value = 5  # Можете изменить значение b для проверки
try:
    z1_result = compute_z1(b_value)
    z2_result = compute_z2(b_value)
    print(f"z1 = {z1_result:.4f}")
    print(f"z2 = {z2_result:.4f}")
except ValueError as e:
    print(e)
