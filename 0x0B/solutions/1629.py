a, b, c = map(int, input().split())


def func(a, b, c):
    if b == 1:
        return a % c
    value = func(a, b // 2, c)
    value = value * value % c
    if b % 2 == 0:
        return value
    else:
        return value * a % c


print(func(a, b, c))
