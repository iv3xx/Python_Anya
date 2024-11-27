def calculate_cost(rubles, kopecks, quantity):
    # Сначала вычислим полную стоимость одного пирожка в копейках
    cost_per_pirozhok_in_kopecks = rubles * 100 + kopecks
    
    # Умножаем на количество пирожков
    total_cost_in_kopecks = cost_per_pirozhok_in_kopecks * quantity
    
    # Переводим обратно в рубли и копейки
    total_rubles = total_cost_in_kopecks // 100
    total_kopecks = total_cost_in_kopecks % 100
    
    return total_rubles, total_kopecks

def get_input():
        while True:
            rubles = int(input("Введите стоимость пирожка (рубли): "))
            kopecks = int(input("Введите стоимость пирожка (копейки): "))
            quantity = int(input("Введите количество пирожков: "))
            
            return rubles, kopecks, quantity
     


A, B, N = get_input()

rubles, kopecks = calculate_cost(A, B, N)

print(f"За {N} пирожков нужно заплатить {rubles} рублей и {kopecks} копеек.")
