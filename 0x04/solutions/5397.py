import sys

c = int(input())

for _ in range(c):
    l = list(sys.stdin.readline().strip())
    left, right = [], []
    for i in range(len(l)):
        if l[i] == '<':
            if left:
                right.append(left.pop())
        elif l[i] == '>':
            if right:
                left.append(right.pop())
        elif l[i] == '-':
            if left:
                left.pop()
        else:
            left.append(l[i])
    print("".join(left) + "".join(reversed(right)))
