from collections import deque

n = int(input())

d = deque([i for i in range(1, n + 1)])

r = d[0]
for _ in range(n):
    if d:
        r = d.popleft()
        if len(d) > 1:
            d.append(d.popleft())

print(r)
