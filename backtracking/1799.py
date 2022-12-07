# 각 칸에 비숍이 있을 때 없을 때(2가지 경우) & 최대 10x10 = 2^100 -> 완탐 불가
# 대각선을 오위 -> 왼아 & 왼위 -> 오아 2개의 경우로 나눠서 풀면 2^(5x5) * 2로 계산 가능
import sys
N = int(input())

# 오위 -> 왼아
# 비숍이 있을 수 있는 칸 모으기
rightTop = []
visited_rightTop = [[False]*N for _ in range(N)]
rightTop_cnt = 0
# 왼위 -> 오아
# 비숍이 있을 수 있는 칸 모으기
leftTop = []
visited_leftTop = [[False]*N for _ in range(N)]
leftTop_cnt = 0

board = []

for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))

for i in range(N):
    for j in range(N):
        if board[i][j] != 1: continue
        if i % 2 == 0 and j % 2 == 0:
            rightTop.append([i, j])
        else:
            leftTop.append([i, j])

def dfs(bishop, idx, cnt):
    global rightTop_cnt, leftTop_cnt
    if idx == len(bishop):
        x, y = bishop[0]
        if x % 2 == 0 and y % 2 == 0:
            rightTop_cnt = max(cnt, rightTop_cnt)
        else:
            leftTop_cnt = max(cnt, leftTop_cnt)
        return

    x, y = bishop[idx]
    if x % 2 == 0 and y % 2 == 0:
        if not visited_rightTop[x][y]:
            visited_rightTop[x][y] = True

    else:
        if not visited_leftTop[x][y]:
            visited_leftTop[x][y] = True



# 2개로 쪼개서 2^(5*5) * 2 계산으로 줄임
if len(rightTop) > 0:
    dfs(rightTop, 0, 0)
if len(leftTop) > 0:
    dfs(leftTop, 0, 0)