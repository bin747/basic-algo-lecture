from collections import deque

vis = [0 for _ in range(100001)]
d = [-1, 1]
queue = deque()

x, y = map(int, input().split())
vis[x] = 1
queue.append(x)
while True:
    pos = queue.popleft()
    if pos == y:
        break
    for dx in d:
        x = pos + dx

        if not 0 <= x <= 100000:
            continue

        if not vis[x] or vis[pos] + 1 < vis[x]:
            vis[x] = vis[pos] + 1
            queue.append(x)

    x = pos * 2
    if not 0 <= x <= 100000:
        continue

    if not vis[x] or vis[pos] < vis[x]:
        vis[x] = vis[pos]
        queue.append(x)

print(vis[y]-1)
