def run_task4():
    user_numb = input("Введите целое положительное число:")
    user_string_len = len(user_numb)
    maximum = 0
    while user_string_len > 0:
        numb = int(user_numb[user_string_len-1])
        user_string_len = user_string_len - 1
        if numb > maximum:
            maximum = numb
        if maximum == 9:
            break
    print(maximum)


