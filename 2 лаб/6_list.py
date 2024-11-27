X = [23, 45, 67, 2, 15, 51, 34, 8, 0, 49, 30]

filtered_elements = [x for x in X if 1 <= x <= 50]

if filtered_elements:
    average = sum(filtered_elements) / len(filtered_elements)
    print(f"Среднее арифметическое элементов списка X, лежащих в интервале [1, 50]: {average:.2f}")
else:
    print("Нет элементов в интервале [1, 50]")
