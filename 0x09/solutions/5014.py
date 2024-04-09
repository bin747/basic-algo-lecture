from collections import deque

f, s, g, u, d = map(int, input().split())

if s == g:
    print(0)
else:
    vis = [0 for _ in range(f)]
    d = [u, -d]

    queue = deque()
    queue.append(s)
    vis[s-1] = 1
    cnt = 0
    result = 0
    while queue:
        pos = queue.popleft()

        for dx in d:
            x = pos + dx

            if not 0 < x <= f:
                continue

            if x == g:
                print(vis[pos - 1])
                quit()

            if not vis[x-1]:
                vis[x-1] = vis[pos-1] + 1
                queue.append(x)
                cnt += 1

    print('use the stairs')