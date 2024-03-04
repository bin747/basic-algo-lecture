n, m, h = map(int, input().split())

if m == 0:
    print(0)
    quit()

board = [[0 for _ in range(n)] for _ in range(h)]

for _ in range(m):
    i, j = map(int, input().split())
    board[i - 1][j - 1] = 1
    board[i - 1][j] = -1


def line(x, y, flag, n, h, board):
    """
    사다리 선 만들기 함수

    Args:
        x, y: 출발지점
        flag: 만들 수 있는 선 개수
        n, h ,board: 사다리 선, 가로선, 사다리 상태

    Returns: check() 했을 때 값
    """
    if flag == 0:
        if check(n, h, board):
            return True
        return False

    for i in range(x, h):
        for j in range(y, n - 1):
            if board[i][j] == 0 and board[i][j + 1] == 0:  # 선 만들 수 있을 때 선 만들고 다음 번부터 선 만들기 진행
                board[i][j] = 1
                board[i][j + 1] = -1

                if line(i, j + 2, flag - 1, n, h, board):
                    return True

                board[i][j] = 0
                board[i][j + 1] = 0
        y = 0  # 가로 줄 만들기 끝나면 0으로 세팅, 안 하면 인자로 들어온 값으로 진행됨


def check(n, h, board):
    """
    사다리 조건 일치 확인

    Args:
        n, h ,board: 사다리 선, 가로선, 사다리 상태

    Returns: 사다리 상태 i -> i로 가는 지 확인
    """
    for i in range(n):
        flag = i
        for j in range(h):
            if board[j][flag] == 1:  # 왼쪽 -> 오른쪽
                flag += 1
            elif board[j][flag] == -1:  # 오른쪽 -> 왼쪽
                flag -= 1
        if flag != i:
            return False
    return True


for i in range(4):
    if line(0, 0, i, n, h, board):
        print(i)
        quit()
print(-1)
