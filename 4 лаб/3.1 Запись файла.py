def write_to_file():
    with open('user_input.txt', 'w') as file:
        while True:
            line = input('Введите строку (или нажмите Enter для завершения): ')
            if line == '':
                break
            file.write(line + '\n')
    print('Данные записаны в файл user_input.txt')

write_to_file()
