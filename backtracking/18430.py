# 이차원 배열 -> 일차원 배열
import sys
N, M = map(int, sys.stdin.readline().split())

graph = []
visited = [False] * (N*M)
# x,y,x,y
boomerang = [[0,-1,1,0],[-1,0,0,-1],[-1,0,0,1],[1,0,0,1]]
answer = 0
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

def dfs(idx, s):
    global visited, answer
    if idx == N*M:
        answer = max(s, answer)
        return
    if visited[idx]:
        return

    # 1차원 idx -> 2차원 n, m
    n = idx // M
    m = idx % M

    visited[idx] = True

    # 부메랑 만들 수 있는 그림 모두 탐색
    for a, b, c, d in boomerang:
        x1 = n+a
        y1 = m+b
        x2 = n+c
        y2 = m+d
        if 0<=x1<N and 0<=y1<M and 0<=x2<N and 0<=y2<M:
            if not visited[x1*M+y1] and not visited[x2*M+y2]:
                visited[x1*M+y1] = True
                visited[x2*M+y2] = True
                new_s = s + graph[n][m] * 2 + graph[x1][y1] + graph[x2][y2]
                for l in range(idx+1, N*M+1):
                    dfs(l, new_s)
                visited[x1*M+y1] = False
                visited[x2*M+y2] = False

    visited[idx] = False

for k in range(N*M):
    dfs(k, 0)


print(answer)