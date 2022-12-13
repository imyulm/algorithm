# 10자리 글자를 재배치 하는 경우의 수: 최대 10! < 1억 -> 완탐
S = list(input())

# 각 문자열 자리 방문 여부
visited = [False] * len(S)

answer = 0
answer_list = []

def dfs(s):
    global answer
    if len(s) == len(S):
        tmp = s[0]
        for i in range(1, len(s)):
            if tmp == s[i]:
                return
            tmp = s[i]
        if str(s) not in answer_list:
            answer += 1
            answer_list.append(str(s))
        return

    for i in range(len(S)):
        if not visited[i]:
            visited[i] = True
            s.append(S[i])
            dfs(s)
            visited[i] = False
            s.pop()


dfs([])
print(answer)