alf = "abcdefghijklmnopqrstuvwxyz"
while True:
    str = input("Введите строку: ")
    c = 0
    for ch in str:
        if ch in alf:
            c+=1
    print("количество прописных английских букв:",c)