n = int(input())

s = []
r = 0
for i in range(n):
    p = int(input())

    while s and s[-1][0] < p:
        r += s.pop()[1]
    if s and s[-1][0] == p:
        cnt = s.pop()[1]
        r += cnt
        if s:
            r += 1
        s.append((p, cnt + 1))
    else:
        if s:
            r += 1
        s.append((p, 1))

print(r)