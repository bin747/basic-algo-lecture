k = int(input())

d = []
for _ in range(k):
    n = int(input())
    if n == 0:
        if d:
            d.pop()
    else:
        d.append(n)
print(sum(d))
