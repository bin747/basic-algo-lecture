n = list(map(int, input()))
d = [0 for _ in range(10)]

for i in range(len(n)):
    d[n[i]] += 1

m = (d[6] + d[9]) // 2 if (d[6] + d[9]) % 2 == 0 else (d[6] + d[9]) // 2 + 1
for i in range(10):
    if i == 6 or i == 9:
        continue
    if m < d[i]:
        m = d[i]
print(m)
