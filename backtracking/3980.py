# 의문
# https://chelseashin.tistory.com/97
# -> 가지치기해서 어떻게 경우의 수 1824개?

import sys
answer = 0
position = []

def dfs(now, selected, sum):
    global answer
    if now == 11:
        answer = max(answer, sum)
        return

    for i in range(11):
        if not selected[i] and position[now][i] > 0:
            selected[i] = True
            dfs(now+1, selected, sum+position[now][i])
            selected[i] = False




T = int(input())
for _ in range(T):
    position = []
    selected = [False]*11
    answer = 0
    for _ in range(11):
        position.append(list(map(int, sys.stdin.readline().split())))

    dfs(0, selected, 0)

    print(answer)
