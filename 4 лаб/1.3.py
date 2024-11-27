def count_unique_words():
    n = int(input("Введите количество строк: "))
    unique_words = set()  

    for _ in range(n):
        line = input()  
        words = line.split() 
        unique_words.update(words)

    print("Количество различных слов:", len(unique_words))


count_unique_words()
