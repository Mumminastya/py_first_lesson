def run_task1():
    a_string = "Donald Duck"
    a_numb = 666
    a_bool = bool(1)
    print(f"string-{a_string} numb-{a_numb} bool-{a_bool}")

    a_string = input("Введите строку: ")
    a_numb = int(input("Введите число: "))
    a_bool = bool(int(input("Познайте истину(1), вкусите ложь(0): ")))
    print(f"string-{a_string} numb-{a_numb} bool-{a_bool}")