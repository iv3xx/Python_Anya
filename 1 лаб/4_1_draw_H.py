def draw_h():
    height = 5  # Высота буквы 
    width = 5   # Ширина буквы 

    for i in range(height):
        for j in range(width):
            
            if j == 0 or j == width - 1 or (i == height // 2):
                print("*", end="")
            else:
                print(" ", end="")
        print()  

draw_h()
