import numpy as np

min = 1
max = 101
number = np.random.randint(1, 101) # загадываем число
count = 0

while True:
    count += 1
    mid = round((min+max) / 2)
    
    if mid > number:
        max = mid
        
    elif mid < number:
        min = mid
        
    else:
        print(f"Вы угадали число! Это число = {number}, за {count} попыток")
        break # конец игры, выход из цикла