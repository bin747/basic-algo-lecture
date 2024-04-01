from collections import deque

n, k = map(int, input().split())
vis = [0 for _ in range(100001)]
board = deque()
board.append(n)
vis[n] = 1

while board:
    pos = board.popleft()
    for i in (pos-1, pos+1, pos*2):
        if 0 <= i <= 100000 and not vis[i]:
            board.append(i)
            vis[i] = vis[pos] + 1
        if i == k:
            print(vis[i] - 1)
            quit()
