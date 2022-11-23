# 민트초코우유 좌표로 dfs
# 우유 선택(선택하면 집돌아올 수 있는지 판변 후 선택) -> dfs -> 우유 선택 풀기
# 우유 선택 순서가 영향이 있는가? 단순히 좌표 순으로 우유를 선택해도 되는가?

import sys

N, M, H = map(int, sys.stdin.readline().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

milks = []
hx = 0
hy = 0
answer = 0

for i in range(N):
    for j in range(N):
        if graph[i][j] == 2:
            milks.append([i, j])
        elif graph[i][j] == 1:
            hx = i
            hy = j


def dfs(x, y, health, milk_cnt):
    global answer

    if abs(x - hx) + abs(y - hy) <= health:
        answer = max(answer, milk_cnt)

    for mx, my in milks:
        if graph[mx][my] == 2:
            d = abs(mx-x) + abs(my-y)
            if health - d >= 0:
                graph[mx][my] = 0
                dfs(mx, my, health-d+H, milk_cnt+1)
                graph[mx][my] = 2


dfs(hx, hy, M, 0)
print(answer)