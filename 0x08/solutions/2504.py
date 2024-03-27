import sys

l = list(sys.stdin.readline().strip())

result = 0
two = 0
three = 0
s = []
isValid = True
for i in range(len(l)):
    if l[i] == "(":
        two += 1
        s.append("(")
    elif l[i] == "[":
        three += 1
        s.append("[")
    elif l[i] == ")":
        if s and s[-1] == "(":
            s.pop()
            two -= 1
            if l[i-1] == "(":
                result += (2 ** two if two > 0 else 1) * (3 ** three if three > 0 else 1) * 2
        else:
            isValid = False
    elif l[i] == "]":
        if s and s[-1] == "[":
            s.pop()
            three -= 1
            if l[i-1] == "[":
                result += (2 ** two if two > 0 else 1) * (3 ** three if three > 0 else 1) * 3
        else:
            isValid = False

if s or not isValid:
    print(0)
else:
    print(result)
