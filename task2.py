def run_task2():
    user_sec = int(input("Введите количество секунд: "))
    H = user_sec // 3600
    M = (user_sec - H * 3600) // 60
    S = user_sec - M * 60 - H * 3600
    print(f'{H:02d}:{M:02d}:{S:02d}')

