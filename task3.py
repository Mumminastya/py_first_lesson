def run_task3():
    user_n = int(input("Введите значение n: "))
    N = user_n + int(f'{user_n}{user_n}') + int(f'{user_n}{user_n}{user_n}')
    print(N)

