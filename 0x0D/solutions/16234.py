# python3, pypy3 둘 다 통과하지만 sys.setrecursionlimit(10**5) 넣어 주어야 함
# 조건에 성립하는 인구 리스트 먼저 찾고, 인구 리스트 돌면서 연합 묶어서 평균 값으로 세팅
# import sys
# sys.setrecursionlimit(10**5)
#
# n, l, r = map(int, sys.stdin.readline().strip().split())
#
# board = []
#
# for _ in range(n):
#     board.append(list(map(int, sys.stdin.readline().strip().split())))
#
# d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
#
#
# def move(move_cnt):
#     pop_list = []
#     for i in range(n):
#         for j in range(n):
#             is_exist = False  # [A] 조건이 성립할 경우 시작 지점은 한 번만 하기 위한 구분키
#             for dx, dy in d:
#                 x, y = i + dx, j + dy
#
#                 if not 0 <= x < n or not 0 <= y < n:
#                     continue
#
#                 diff = abs(board[i][j] - board[x][y])
#                 if l <= diff <= r:  # [A] 조건
#                     is_exist = True
#                     if not (x, y) in pop_list:  # 인구 리스트에 추가
#                         pop_list.append((x, y))
#             if is_exist and not (i, j) in pop_list: # 시작 지점이 인구 리스트에 없을 때만 추가 (중복 방지)
#                 pop_list.append((i, j))
#     if not pop_list:  # 인구 리스트 없으면 return
#         return move_cnt
#
#     for i in range(len(pop_list)):  # 인구 리스트 돌면서 연합들 끼리 묶어줌
#         if pop_list[i]:
#             cnt = 0
#             union = [pop_list[i]]  # 연합 여부 확인
#             visit = [pop_list[i]]  # 연합 여부 확인하면서 pop을 해버리니 연합인 애들 묶어 주는 키
#             while union:
#                 pos = union.pop()
#                 cnt += board[pos[0]][pos[1]]
#                 for dx, dy in d:
#                     x, y = pos[0] + dx, pos[1] + dy
#
#                     if not 0 <= x < n or not 0 <= y < n:
#                         continue
#
#                     diff = abs(board[pos[0]][pos[1]] - board[x][y])
#                     if not (x, y) in visit and (x, y) in pop_list and l <= diff <= r:
#                         union.append((x, y))
#                         visit.append((x, y))
#
#             data = cnt // len(visit)
#
#             while visit:  # 연합 돌면서 평균 값으로 세팅
#                 pos = visit.pop()
#                 board[pos[0]][pos[1]] = data
#                 pop_list[pop_list.index(pos)] = False  # 사용한 인구 리스트는 False로 변경
#
#     return move(move_cnt + 1)
#
#
# print(move(0))


# python3 시간 초과, pypy3만 통과
# 리스트 전체 돌면서 연합 발생할 때마다 평균 값으로 세팅
import sys

n, l, r = map(int, sys.stdin.readline().strip().split())

board = []

for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().strip().split())))

d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

move_cnt = 0
is_exist = True
visit = [[False for _ in range(n)] for _ in range(n)]  # 방문 여부
visit_list = []  # 방문한 위치
while is_exist:
    is_exist = False
    for i in range(n):
        for j in range(n):
            if not visit[i][j]:
                population = [(i, j)]
                group = [(i, j)]
                visit[i][j] = True
                visit_list.append((i, j))
                cnt = board[i][j]
                size = 1
                while population:
                    pos = population.pop()

                    for dx, dy in d:
                        x, y = pos[0] + dx, pos[1] + dy

                        if not 0 <= x < n or not 0 <= y < n:
                            continue

                        diff = abs(board[pos[0]][pos[1]] - board[x][y])
                        if l <= diff <= r and not visit[x][y]:
                            visit[x][y] = True
                            cnt += board[x][y]
                            size += 1
                            population.append((x, y))
                            group.append((x, y))
                            visit_list.append((x, y))

                if size > 1:  # 조건 성립한다면
                    is_exist = True
                    data = cnt // size
                    while group:  # 연합의 평균값 세팅
                        pos = group.pop()
                        board[pos[0]][pos[1]] = data
                else:  # 조건 성립하는 것 없으면 방문한 애들 원복
                    visit[i][j] = False
                    visit_list.pop()
    while visit_list:
        pos = visit_list.pop()
        visit[pos[0]][pos[1]] = False
    if is_exist:
        move_cnt += 1
print(move_cnt)
