n = int(input())

for _ in range(n):
    a, b = input().split()
    if len(a) != len(b):
        print('Impossible')
        continue
    before = sorted(list(a))
    after = sorted(list(b))
    print('Possible' if before == after else 'Impossible')