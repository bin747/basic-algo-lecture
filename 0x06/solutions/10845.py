import sys

c = int(input())

q = []
for _ in range(c):
    l = list(sys.stdin.readline().strip().split())

    if l[0] == 'push':
        q.append(l[1])
    elif l[0] == 'pop':
        if q:
            print(q[0])
            q.remove(q[0])
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
            print(q[0])
        else:
            print(-1)
    elif l[0] == 'back':
        if q:
            print(q[len(q)-1])
        else:
            print(-1)