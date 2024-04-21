from collections import deque

n, k = map(int, input().split())

dist = [-1 for _ in range(500001)]
odd_vis = [0 for _ in range(500001)]
even_vis = [0 for _ in range(500001)]

queue = deque()
d = [-1, 1]

if n == k:
    print(0)
else:
    dist[n] = 0
    even_vis[n] = 1

    queue.append(n)

    moveCnt = 0
    while queue:
        pos = queue.popleft()
        if pos != 0:
            d.append(pos)

        for dx in d:
            x = pos + dx

            if not 0 <= x <= 500000:
                continue
            if dist[pos] + 1 > moveCnt:
                moveCnt += 1
                k += moveCnt
                if k > 500000:
                    print(-1)
                    quit()

            # 짝수/홀수 초일 때 해당 짝수/홀수칸(x초일 때 동생이 이동한 수) 방문한 적 있으면 +, - 하면 똑같은 값 이므로 방문 가능함
            if x == k or moveCnt % 2 == 0 and even_vis[k] == 1 or moveCnt % 2 == 1 and odd_vis[k] == 1:
                print(moveCnt)
                quit()

            if moveCnt % 2 == 0 and not even_vis[x]:  # 짝수 초일 땐 짝수만
                even_vis[x] = 1
                queue.append(x)
                if dist[x] == dist[pos]:    # pos 와 x를 append 한 moveCnt 가 같고 홀수/짝수 초에 방문한 것만 다를 때 moveCnt 세팅 넘어감
                    continue
                dist[x] = dist[pos] + 1
            if moveCnt % 2 != 0 and not odd_vis[x]:  # 홀수 초일 땐 홀수만
                odd_vis[x] = 1
                queue.append(x)
                if dist[x] == dist[pos]:
                    continue
                dist[x] = dist[pos] + 1

        if pos != 0:
            d.pop()