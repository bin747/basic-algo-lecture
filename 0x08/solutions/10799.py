import sys

n = list(sys.stdin.readline().strip())

s = []
result = 0
for i in range(len(n)):
    if n[i] == "(":
        s.append(n[i])
    else:
        if n[i-1] == "(":
            s.pop()
            result += len(s)
        else:
            result += 1
            s.pop()
print(result)