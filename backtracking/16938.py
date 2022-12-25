import sys

# N: 문제 개수, L: 문제 최저 난이도, R: 문제 최고 난이도, X: R-L의 최소 차이
N, L, R, X = map(int, sys.stdin.readline().split())

A_list = list(map(int, sys.stdin.readline().split()))

answer_list = set()

# 2문제 이상 골라야 함
# 중복 불가 조합
def dfs(idx, selected):
    global answer
    if len(selected) >= 2:
        sum_A = 0
        tmp_L = 10000000000
        tmp_R = 0
        for A in selected:
            sum_A += A
            tmp_L = min(tmp_L, A)
            tmp_R = max(tmp_R, A)

        if (L <= sum_A <= R) and (tmp_R - tmp_L >= X):
            answer_list.add(str(selected))
        return

    for i in range(idx, N):
        selected.append(A_list[i])
        dfs(idx+1, selected)
        selected.pop()
        dfs(idx+1, selected)



dfs(0, list())
print(len(answer_list))
