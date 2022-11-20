# 만족해야 하는 값을 DFS의 인자로 넘기게 하기
# -> 단백질, 지방,,, 합을 인자로 넘김
import sys
N = int(input())

m = list(map(int, sys.stdin.readline().split()))
mc = 100000
mc_list = []

ingredient = []
for _ in range(N):
    ingredient.append(list(map(int, sys.stdin.readline().split())))

def dfs(idx, in_sum, idx_list):
    global mc, mc_list
    # 만족해야 하는 조건

    # 1. 최소비용이어야 함
    if mc <= in_sum[4]:
        return
    # 2. 식재료 각 영양분 합이 최소를 넘어야 함
    for i in range(4):
        if in_sum[i] < m[i]:
            break
    else:
        mc = in_sum[4]
        mc_list = idx_list[:]
        return
    # 3. depth가 주어진 식재료 개수까지 가면 끝
    if idx == N:
        return

    idx_list.append(idx+1)
    for i in range(5):
        in_sum[i] += ingredient[idx][i]
    dfs(idx+1, in_sum, idx_list)

    idx_list.pop()
    for i in range(5):
        in_sum[i] -= ingredient[idx][i]
    dfs(idx+1, in_sum, idx_list)


dfs(0, [0]*5, [])
if mc == 100000:
    print(-1)
else:
    print(mc)
    for i in mc_list:
        print(i, end=' ')