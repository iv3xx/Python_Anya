import keyboard  # Импортируем библиотеку keyboard

def sum_numbers():
    total = 0
    print("Введите числа для суммирования. Нажмите пробел для завершения.")

    while True:
        try:
            if keyboard.is_pressed('space'):
                print("\nСуммирование завершено.")
                print(f"Итоговая сумма: {total}")
                break

            number = input("Введите число (или нажмите пробел для завершения): ")  
            
            if number == "":
                continue  

            if keyboard.is_pressed('space'):
                print("\nСуммирование завершено.")
                print(f"Итоговая сумма: {total}")
                break
            
            total += float(number)  
            print(f"Текущая сумма: {total}")  

        except ValueError:  
            print("Пожалуйста, введите корректное число.")

sum_numbers()
