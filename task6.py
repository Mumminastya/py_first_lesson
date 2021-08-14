def run_task6():
    a = int(input("Введите значение a: "))
    b = int(input("Введите значение b: "))
    jud_day = 1
    while a <= b:
        a = a * 1.1
        jud_day += 1
    print(jud_day)

