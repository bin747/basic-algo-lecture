import sys

s = []
r = []

k = int(input())

flag = 1
i = 1
j = 0
while True:
    if flag and j < k:
        inp = int(input())   
        flag = 0
        j += 1

    if s and s[len(s) - 1] == inp:
        r.append('-')
        s.pop()
        flag = 1
    else:
        if i > k:
            break
        r.append('+')
        s.append(i)
        i += 1

if s:
    print('NO')
else:
    for i in range(len(r)):
        print(r[i])