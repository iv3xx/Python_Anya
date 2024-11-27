products = [
    {"name": "Товар A", "quantity": 10, "price": 150.75},
    {"name": "Товар B", "quantity": 5, "price": 200.50},
    {"name": "Товар C", "quantity": 8, "price": 100.00},
    {"name": "Товар D", "quantity": 2, "price": 500.00},
    {"name": "Товар E", "quantity": 12, "price": 75.25},
]

print(f"{'Товар':<15} {'Количество':<12} {'Цена (р.)':<10} {'Сумма (р.)':<10}")
print('-' * 50)

for product in products:
    total_sum = product["quantity"] * product["price"]
    print(f"{product['name']:<15} {product['quantity']:<12} {product['price']:<10.2f} {total_sum:<10.2f}")
