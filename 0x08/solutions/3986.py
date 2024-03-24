import sys

n = int(input())

count = 0
for _ in range(n):
    arr = []
    s = list(sys.stdin.readline().strip())
    if len(s) % 2 != 0:
        continue
    for i in range(len(s)):
        if len(arr) == 0:
            arr.append(s[i])
        else:
            if arr[-1] == s[i]:
                arr.pop()
            else:
                arr.append(s[i])

    if len(arr) == 0:
        count += 1

print(count)
