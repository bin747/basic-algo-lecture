import sys

n = int(input())

s = []
s_in = []

r = []
t = list(map(int, sys.stdin.readline().strip().split()))

for i in range(len(t)):
    for j in range(len(s), 0, -1):
        if s[j-1] <= t[i]:
            s.pop()
            s_in.pop()
        else:
            break
    r.append(s_in[len(s_in)-1] if len(s_in) != 0 else 0)
    s_in.append(i+1)
    s.append(t[i])

for i in range(len(r)):
    print(r[i], end=' ')
