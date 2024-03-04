import sys
from collections import deque

c = int(input())

q = deque([])
for _ in range(c):
    l = list(sys.stdin.readline().strip().split())

    if l[0] == 'push':
        q.append(l[1])
    elif l[0] == 'pop':
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif l[0] == 'size':
        print(len(q))

    elif l[0] == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif l[0] == 'front':
        if q:
            a = q.popleft()
            print(a)
            q.appendleft(a)
        else:
            print(-1)
    elif l[0] == 'back':
        if q:
            a = q.pop()
            print(a)
            q.append(a)
        else:
            print(-1)