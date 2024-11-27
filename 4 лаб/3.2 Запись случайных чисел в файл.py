import random

# Генерация случайных чисел и запись в файл
def generate_numbers(filename, count=10, lower_bound=1, upper_bound=100):
    with open(filename, 'w') as file:
        for _ in range(count):
            number = random.randint(lower_bound, upper_bound)
            file.write(f"{number}\n")

# Чтение чисел из файла и нахождение суммы чётных чисел
def sum_even_numbers(filename):
    even_sum = 0
    with open(filename, 'r') as file:
        for line in file:
            number = int(line.strip())
            if number % 2 == 0:
                even_sum += number
    return even_sum


filename = 'random_numbers.txt'
generate_numbers(filename)  
sum_of_evens = sum_even_numbers(filename)  

print(f"Сумма чётных чисел: {sum_of_evens}")
