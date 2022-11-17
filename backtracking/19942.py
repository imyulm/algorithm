import sys

N = int(input())
protein = [0]
fat = [0]
sugar = [0]
vitamin = [0]
cost = [0]
select_cnt = 1
find_yn = False
selected = []
selected_yn = [True] + [False] * N
answer_selected = []
answer_cost = 10000

mp, mf, ms, mv = map(int, sys.stdin.readline().split())

for _ in range(N):
    p, f, s, v, c = map(int, sys.stdin.readline().split())
    protein.append(p)
    fat.append(f)
    sugar.append(s)
    vitamin.append(v)
    cost.append(c)

def dfs():
    global answer_cost, answer_selected, find_yn
    if len(selected) == select_cnt:
        tp = 0
        tf = 0
        ts = 0
        tv = 0
        tc = 0
        for i in selected:
            tp += protein[i]
            tf += fat[i]
            ts += sugar[i]
            tv += vitamin[i]
            tc += cost[i]
        if answer_cost < tc:
            return
        if tp >= mp and tf >= mf and ts >= ms and tv >= mv:
            if answer_cost > tc:
                answer_selected = selected[:]
                answer_cost = tc
                find_yn = True
        return

    for j in range(1, N+1):
        if not selected_yn[j]:
            selected_yn[j] = True
            selected.append(j)
            dfs()
            selected.remove(j)
            selected_yn[j] = False



for cnt in range(1,N+1):
    select_cnt = cnt
    dfs()
    if find_yn:
        break
    selected = []
if answer_cost != 10000:
    print(answer_cost)
    print(*answer_selected)
else:
    print("-1")