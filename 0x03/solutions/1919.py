first = list(input())
second = list(input())

firstCount = [0 for _ in range(26)]
secondCount = [0 for _ in range(26)]

for i in range(len(first)):
    firstCount[ord(first[i]) - 97] += 1
for i in range(len(second)):
    secondCount[ord(second[i]) - 97] += 1

cnt = 0
for i in range(26):
    cnt += (firstCount[i] - secondCount[i] if firstCount[i] >= secondCount[i] else secondCount[i] - firstCount[i])
print(cnt)
