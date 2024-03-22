import sys
from collections import deque

t = int(input())

for _ in range(t):
    p = list(map(str, sys.stdin.readline().strip()))
    n = int(input())
    x = sys.stdin.readline().strip()
    x = deque() if x == '[]' else deque(x[1:-1].split(','))

    reverse = False
    isError = False
    for i in range(len(p)):
        if p[i] == 'R':
            reverse = not reverse
        if p[i] == 'D':
            if len(x) == 0:
                isError = True
                break
            if reverse:
                x.pop()
            else:
                x.popleft()
    if isError:
        print('error')
    else:
        if reverse:
            x.reverse()
        print('[' + ','.join(x) + ']')
