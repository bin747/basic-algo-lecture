n = int(input())
d = sorted(list(map(int, input().split())))
x = int(input())

cnt = 0
s = 0
e = n - 1
while s < e:
    if d[s] + d[e] == x:
        s += 1
        e -= 1
        cnt += 1
    elif d[s] + d[e] > x:
        e -= 1
    else:
        s += 1
print(cnt)
