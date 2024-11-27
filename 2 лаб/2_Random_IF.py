import random


random_number = random.randint(0, 100)
print(f"Сгенерированное число: {random_number}")

remainder = random_number % 3

if remainder == 0:
    print("Остаток от деления на 3 равен 0. Это число делится на 3!")
elif remainder == 1:
    print("Остаток от деления на 3 равен 1. Это число не делится на 3!")
else:  # remainder == 2
    print("Остаток от деления на 3 равен 2. Это число также не делится на 3!")
