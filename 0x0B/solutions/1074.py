def func(n, r, c):
    if n == 0:
        return 0
    half = 2 ** (n - 1)

    if r < half and c < half:
        return func(n - 1, r, c)
    elif r < half <= c:
        return func(n - 1, r, c - half) + half * half
    elif r >= half > c:
        return func(n - 1, r - half, c) + 2 * half * half

    return func(n - 1, r - half, c - half) + 3 * half * half


n, r, c = map(int, input().split())
print(func(n, r, c))