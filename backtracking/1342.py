# 1. return 하는 부분에서 조건에 맞는지 확인 하는 방법
# 10자리 글자를 재배치 하는 경우의 수: 최대 10! < 1억 -> 완탐
# 시간초과 : 전체 경우의 수가 1억 미만이어도 if not in 으로 찾는다거나 할 때 시간초과가 날 수 있음 주의 -> set 사용
S = list(input())

# 각 문자열 자리 방문 여부
visited = [False] * len(S)

answer_list = set()

def dfs(s):
    if len(s) == len(S):
        tmp = s[0]
        for i in range(1, len(s)):
            if tmp == s[i]:
                return
            tmp = s[i]
        answer_list.add(str(s))
        return

    for i in range(len(S)):
        if not visited[i]:
            visited[i] = True
            s.append(S[i])
            dfs(s)
            visited[i] = False
            s.pop()


dfs([])
print(len(answer_list))