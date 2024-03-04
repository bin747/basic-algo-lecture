s = list(input())

d = [0 for _ in range(26)]
for i in range(len(s)):
    d[ord(s[i])-97] += 1

for i in range(26):
    print(d[i], end=' ')