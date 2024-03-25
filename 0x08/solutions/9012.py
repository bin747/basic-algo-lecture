import sys

t = int(input())
for _ in range(t):
    s = []
    isValid = True
    l = list(sys.stdin.readline().strip())
    for i in range(len(l)):
        if l[i] == "(":
            s.append("(")
        else:
            if s and s[-1] == "(":
                s.pop()
            else:
                isValid = False
                break
    if s or not isValid:
        print("NO")
    else:
        print("YES")
