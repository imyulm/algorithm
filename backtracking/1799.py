# 각 칸에 비숍이 있을 때 없을 때(2가지 경우) & 최대 10x10 = 2^100 -> 완탐 불가
# 대각선을 오위 -> 왼아 & 왼위 -> 오아 2개의 경우로 나눠서 풀면 2^(5x5) * 2로 계산 가능

import sys
N = int(input())

# 대각선 종류 2가지
# 1. 오위 -> 왼아
visited_rightTop = [False]*(N*2-1)
# 2. 왼위 -> 오아
visited_leftTop = [False]*(N*2-1)

# 비숍이 있을 수 있는 칸 모으기
# 1. (0,0), (0,2), (2,0), (1,1) ...
bishop1 = []
bishop1_cnt = 0

# 2. (1,0), (0,1), (0,3), (1,2), (2,1), (3,0) ...
bishop2 = []
bishop2_cnt = 0

board = []

for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))

for i in range(N):
    for j in range(N):
        if board[i][j] != 1: continue
        # 비숍이 있을 수 있는 칸 (1번)
        if (i % 2 == 0 and j % 2 == 0) or (i % 2 != 0 and j % 2 != 0):
            bishop1.append([i, j])
        # 비숍이 있을 수 있는 칸 (2번)
        else:
            bishop2.append([i, j])

def dfs(bishop, idx, cnt):
    global bishop1_cnt, bishop2_cnt
    if idx == len(bishop):
        # 비숍이 있을 수 있는 칸 중 어떤 유형인지
        x, y = bishop[0]
        # 비숍이 있을 수 있는 칸 (1번)
        if (x % 2 == 0 and y % 2 == 0) or (x % 2 != 0 and y % 2 != 0):
            bishop1_cnt = max(cnt, bishop1_cnt)
        # 비숍이 있을 수 있는 칸 (2번)
        else:
            bishop2_cnt = max(cnt, bishop2_cnt)
        return

    x, y = bishop[idx]
    # 2개 대각선 중 하나라도 해당자리와 겹치는 경우(1-1)
    if visited_rightTop[x+y] or visited_leftTop[x-y+N-1]:
        dfs(bishop, idx+1, cnt)
    else:
        visited_rightTop[x+y] = True
        visited_leftTop[x-y+N-1] = True
        # 해당 자리에 비숍 놓는 경우(2-1)
        dfs(bishop, idx+1, cnt+1)
        visited_rightTop[x+y] = False
        visited_leftTop[x-y+N-1] = False
        # 2개 대각선 아무것도 해당 자리에 걸치지 않고(1-2) 해당 자리에 비숍을 놓지 않는 경우(2-2)
        dfs(bishop, idx + 1, cnt)


# 2개로 쪼개서 2^(5*5) * 2 계산으로 줄임
if len(bishop1) > 0:
    dfs(bishop1, 0, 0)
if len(bishop2) > 0:
    dfs(bishop2, 0, 0)

print(bishop1_cnt + bishop2_cnt)