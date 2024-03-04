import sys

c = int(input())

s = []
for _ in range(c):
    l = list(sys.stdin.readline().strip().split())

    if l[0] == 'push':
        s.append(l[1])
    elif l[0] == 'pop':
        if s:
            print(s.pop())
        else:
            print(-1)
    elif l[0] == 'size':
        print(len(s))

    elif l[0] == 'empty':
        if len(s) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(s) > 0:
            print(s[len(s)-1])
        else:
            print(-1)
