# 2. return 하는 부분에서 조건에 맞는지 확인 x
# for문 돌면서 다음 dfs 넣기 전에 조건에 맞는지 확인

def dfs(cnt, string):
    global N, answer

    if cnt == N:
        answer += 1
        return

    # 종류별로 알파벳 검사(알파벳 갯수마다)
    for char in char_set:
        idx = ord(char) - 97
        # 알파벳 다썼으면 패스
        if char_cnt[idx] == 0:
            continue
        # string 이 있고 전에 넣은게 지금꺼랑 같으면 패스
        if string and string[-1] == char:
            continue

        char_cnt[idx] -= 1
        dfs(cnt + 1, string + char)
        char_cnt[idx] += 1


S = input()
# 각 알파뱃 개수 담는 배열
# idx = ord('a')기준 0 -97해주면됨.
char_cnt = [0] * 26
N = len(S)
answer = 0
# 어떤 알파벳 있는지
char_set = set()

# ord('a') = 97
# 어떤 알파벳 있는지(char_set) + 각 알파벳의 갯수(char_cnt)
for char in S:
    idx = ord(char) - 97
    char_cnt[idx] = char_cnt[idx] + 1
    char_set.add(char)


dfs(0, '')
print(answer)