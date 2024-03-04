import sys

n = int(input())

s = []
s_in = []
t = []
r = []
for _ in range(n):
    t.append(int(sys.stdin.readline().strip()))
t.reverse()

for i in range(n):
    for j in range(len(s), 0, -1):
        if s[j-1] < t[i]:
            s.pop()
            s_in.pop()
        else:
            break
    r.append(s_in[len(s_in)-1] if len(s_in) != 0 else 0)
    s_in.append(i+1)
    s.append(t[i])

t.reverse()
r.reverse()

cnt = 0
for i in range(n):
    if r[i] == 0:
        cnt += len(t) - i - 1
    else:
        cnt += len(t) - r[i] - i - 1 if len(t) - r[i] - i - 1 > 0 else 0

print(cnt)
