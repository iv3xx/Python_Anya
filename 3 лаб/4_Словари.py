def calculate_total_purchases(purchases):
    total_spent = {}  # Словарь для хранения общей суммы покупок

    for name, amounts in purchases.items():
        total_spent[name] = sum(amounts)  # Суммируем все суммы для каждого покупателя

    return total_spent

# Пример использования функции
purchases_dict = {
    "Alice": [150.50, 200.00, 89.99],
    "Bob": [99.99, 34.50],
    "Charlie": [120.00, 200.75, 50.50],
    "David": [75.00, 125.00, 250.00, 10.50],
    "Eva": [300.00, 400.00],
    "Frank": [55.50, 45.50, 60.00, 150.00],
    "Grace": [95.00, 20.00, 15.00],
    "Hank": [200.00, 300.00, 150.00, 450.00],
    "Ivy": [400.00, 250.00],
    "Jack": [88.88, 111.11, 222.22],
}

total_purchases = calculate_total_purchases(purchases_dict)
print(total_purchases)
