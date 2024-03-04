import sys
from collections import deque

n = int(input())

q = deque([])

for _ in range(n):
    l = list(sys.stdin.readline().strip().split())

    if l[0] == 'push_front':
        q.appendleft(l[1])
    elif l[0] == 'push_back':
        q.append(l[1])
    elif l[0] == 'pop_front':
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif l[0] == 'pop_back':
        if q:
            print(q.pop())
        else:
            print(-1)
    elif l[0] == 'size':
        print(len(q))
    elif l[0] == 'empty':
        if q:
            print(0)
        else:
            print(1)
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