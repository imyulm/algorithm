# 각 칸에 비숍이 있을 때 없을 때(2가지 경우) & 최대 10x10 = 2^100 -> 완탐 불가
# 대각선을 오위 -> 왼아 & 왼위 -> 오아 2개의 경우로 나눠서 풀면 2^(5x5) * 2로 계산 가능
import sys
N = int(input())

# 오위 -> 왼아
rightTop = []
visited_rightTop = [[False]*N for _ in range(N)]
rightTop_cnt = 0
# 왼위 -> 오아
leftTop = []
visited_leftTop = [[False]*N for _ in range(N)]
leftTop_cnt = 0

board = []

answer = 0

for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))

for i in range(N):
    for j in range(N):
        if board[i][j] != 1: continue
        if i % 2 == 0 and j % 2 == 0:
            rightTop.append([i, j])
        else:
            leftTop.append([i, j])

def dfs(bishop, visited, cnt):
    global answer




# 2개로 쪼개서 2^(5*5) * 2 계산으로 줄임
if len(rightTop) > 0:
    dfs(rightTop, visited_rightTop, 0)
if len(leftTop) > 0:
    dfs(leftTop, visited_leftTop, 0)