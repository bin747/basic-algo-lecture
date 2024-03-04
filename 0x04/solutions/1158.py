import sys

k, n = map(int, sys.stdin.readline().split())
d = [i for i in range(1, k+1)]

a = []
flag = 0
for _ in range(k):
    flag += n - 1
    if flag >= len(d):
        flag = flag % len(d)
    a.append(d.pop(flag % len(d)))
print('<', end='')
for i in range(len(a)-1):
    print(a[i], end=', ')
print(a[len(a)-1], end='')
print('>')