from collections import deque

n, k = map(int, input().split())

vis = [0 for _ in range(100001)]
visList = {}

d = [-1, 1]
queue = deque()

vis[n] = 1
visList[-1] = n
queue.append(n)

while queue:
    pos = queue.popleft()

    d.append(pos)
    for dx in d:
        x = pos + dx

        if not 0 <= x <= 100000:
            continue

        if not vis[x]:
            vis[x] = vis[pos] + 1
            visList[x] = pos
            queue.append(x)

        if x == k:
            print(vis[k] - 1)
            if vis[k] == 1:
                print(k)
            else:
                result = [k]
                x = k
                while visList.get(x) and visList.get(x) != n:
                    result.append(visList[x])
                    x = visList[x]
                result.append(n)
                print(*result[::-1], end=" ")
            quit()
    d.pop()
