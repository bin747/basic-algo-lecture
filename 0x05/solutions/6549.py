import sys

while True:
    s = []
    result = 0
    l = list(map(int, sys.stdin.readline().strip().split()))
    if l[0] == 0:
        break
    else:
        for i in range(1, len(l)):
            if s and s[-1][1] > l[i]:
                while s:
                    stack_i, stack_height = s.pop()
                    width_start = 1
                    if s:
                        width_start = s[-1][0]+1
                    result = max(result, (i - width_start) * stack_height)
                    if not s or s[-1][1] <= l[i]:
                        break
            if not s or s[-1][1] <= l[i]:
                s.append((i, l[i]))
    while s:
        stack_i, stack_height = s.pop()
        width_start = 1
        if s:
            width_start = s[-1][0]+1
        result = max((l[0]+1 - width_start) * stack_height, result)

    print(result)