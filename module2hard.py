def shifr(k, j):
    list_ = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    key1 = []
    key2 = []
    import random
    for i in range(3, 21):
        i = random.choice(list_[i])
    for (k, j) in range(1, i):
        k = True
        j = True
    if 1 <= k <= i and 1 <= j <= i:
        k = True
        j = True
    elif k + j <= i:
        k = True
        j = True
    elif (k + j) % i == 0:
        k = True
        j = True
        key1.append(key1)
        key2.append(key2)

        print(k, j)
