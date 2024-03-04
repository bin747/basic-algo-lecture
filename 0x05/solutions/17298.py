import sys

n = int(input())

s = []
s_in = []
t = []
r = []
t = list(map(int, sys.stdin.readline().strip().split()))
t.reverse()

for i in range(n):
    for j in range(len(s), 0, -1):
        if s[j-1] <= t[i]:
            s.pop()
            s_in.pop()
        else:
            break
    r.append(s_in[len(s_in)-1] if len(s_in) != 0 else -1)
    s_in.append(i+1)
    s.append(t[i])

t.reverse()
r.reverse()

for i in range(n):
    print(t[len(t)-r[i]] if r[i] != -1 else -1, end=' ')