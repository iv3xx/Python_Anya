import random

a = int(input("Введите значение a: "))
random_number = random.uniform(-a, a)
print(f"Сгенерированное случайное число: {random_number:.2f}")


user_number = float(input("Введите число для проверки: "))


if -a <= user_number <= a:
    print(f"Число {user_number} входит в диапазон [-{a}, {a}].")
else:
    print(f"Число {user_number} НЕ входит в диапазон [-{a}, {a}].")
