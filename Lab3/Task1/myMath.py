

def add(x, y):
    return x + y


def subtraction(x, y):
    return int(x) - int(y)


def evenNumber(list):
    count = 0
    for i in list:
        if int(i) % 2 == 0:
            count = count + 1
    return count


def maximum(list):
    return max(list)


def minumum(list):
    return min(list)


def absolute(x):
    return abs(x)


def sumTotal(list):
    total = 0

    for i in list:
        total = int(total) + int(i)
    return total


def clear(tituus):
    if (int(minumum(tituus))<5):

        for index, i in enumerate(tituus):
            tituus[index] = 0
        return tituus
    else:
        return tituus
