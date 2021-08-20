def run_task2():
    user_sec = int(input("Введите количество секунд: "))
    h = user_sec // 3600
    m = (user_sec - h * 3600) // 60
    s = user_sec - m * 60 - h * 3600
    print(f'{h:02d}:{m:02d}:{s:02d}')

