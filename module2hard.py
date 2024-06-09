
n = int(input('Введите число от 3 до 20:'))


def find_password(n):
    result = list()
    for i in range(1, n):
        for j in range(i + 1, n):
            if n % (i + j) == 0:
                result.append(str(i) + str(j))
    return result


get_result = find_password(n)
print(str(n) + ' - ' + ''.join([str(x) for x in get_result]))
