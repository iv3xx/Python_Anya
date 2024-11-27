def ameba_count(k):
    # Начальное количество амеб
    count = 1
    
    # Количество делений
    divisions = 0
    
    while divisions * 3 < k:
        count *= 2  
        divisions += 1
        
    return count

k = int(input("Введите количество часов (k): "))
result = ameba_count(k)
print(f"Через {k} часов будет {result} амеб.")
