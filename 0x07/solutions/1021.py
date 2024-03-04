import sys
from collections import deque

n, m = map(int, sys.stdin.readline().strip().split())
d = deque(map(int, sys.stdin.readline().strip().split()))
q = deque([i for i in range(1, n + 1)])

cnt = 0
while d:
    find = d.popleft()
    while True:
        if q[0] == find:
            q.popleft()
            break
        else:
            index = q.index(find)
            if index <= len(q)//2:
                q.append(q.popleft())
                cnt += 1
            else:
                q.appendleft(q.pop())
                cnt += 1
print(cnt)
