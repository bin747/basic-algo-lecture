import sys

t = int(input())


def bfs(index, result):
    vis[index] = True
    cycle.append(index)
    queue.append(team[index] - 1)

    while queue:
        pos = queue.pop()
        if vis[pos]:
            if pos in cycle:
                result += cycle[cycle.index(pos):]
            return
        else:
            vis[pos] = True
            cycle.append(pos)
            queue.append(team[pos] - 1)


for _ in range(t):
    n = int(input())
    team = list(map(int, sys.stdin.readline().strip().split()))
    vis = [False for _ in range(n)]
    cntList = []
    for i in range(n):
        if not vis[i]:
            cycle = []
            queue = []
            bfs(i, cntList)
    print(n - len(cntList))