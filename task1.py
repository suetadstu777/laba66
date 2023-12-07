while True:
    str = input("Введите строку:")
    new_str = ''
    flag = False
    for ch in str:
        if ch == ")":
            flag  =False
        if not flag:
            new_str+=ch
        if ch == "(":
            flag = True
    print('Новая строка: ')
    print(new_str)