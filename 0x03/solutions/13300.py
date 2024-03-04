n, k = map(int, input().split())

girl = [0 for _ in range(6)]
boy = [0 for _ in range(6)]

for _ in range(n):
    s, y = map(int, input().split())
    if s == 0:
        girl[y - 1] += 1
    else:
        boy[y - 1] += 1

cnt = 0
for i in range(6):
    cnt += (girl[i] // k if girl[i] % k == 0 else girl[i] // k + 1)
    cnt += (boy[i] // k if boy[i] % k == 0 else boy[i] // k + 1)

print(cnt)
