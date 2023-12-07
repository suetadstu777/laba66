import random

while True:
    while True:
        try:
            inp = int(input("Введите длинну массива: "))
        except ValueError:
            print("неверные данные, введите число")
    list = [random.randint(-10,10) for _ in range(0,inp)]
    zero_c = 0
    min_n = 11
    for n in list:
        if n == 0:
            zero_c +=1
        if n<min_n:
            min_n = n

    flag = False
    c_posle_min = 0
    for n in list:
        if flag:
            c_posle_min+=n
        if n == min_n:
            flag = True
    print("Cписок:",list)
    print("Кол-во нолей:",zero_c)
    print("Сумма после минимального элемента",c_posle_min)


