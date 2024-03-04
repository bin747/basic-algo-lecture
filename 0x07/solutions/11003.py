import sys
from collections import deque

l, n = list(map(int, sys.stdin.readline().strip().split()))
a = list(map(int, sys.stdin.readline().strip().split()))

s = deque()
for i in range(l):
    if s:
        if len(s) == n or s[0] <= i-n:
            s.popleft()

    while s:
        before = s.pop()
        if a[before] <= a[i]:
            s.append(before)
            break
    s.append(i)
    print(a[s[0]], end=' ')
