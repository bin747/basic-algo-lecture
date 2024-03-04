n = int(input())
d = list(map(int, input().split()))
v = int(input())

cnt = 0
for i in range(len(d)):
    if d[i] == v:
        cnt += 1
print(cnt)
