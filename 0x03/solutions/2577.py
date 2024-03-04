a = int(input())
b = int(input())
c = int(input())

r = str(a * b * c)
d = [0 for _ in range(10)]

for i in range(len(r)):
    d[int(r[i])] += 1

for i in range(10):
    print(d[i])
