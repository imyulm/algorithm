# 즐거운 단어 : 모음(A, E, I, O, U) 연속 3번 X, 자음은 연속 3번 X , L 반드시 포함
# dfs 넘겨줄 변수 : 밑줄 idx, 여태껏 완성한 단어, L 포함여부, 가능 단어 개수
# 밑줄에 들어갈 수 있는 알파벳 : L 제외 자음, 모음, L -> dfs 안에 for문에서 사용
from collections import defaultdict

word = input()
LYn = False
underba = []

answer = 0
# L, 자음 21, 모음 5
alphabets = ['엘', '자', '모']

for i in range(len(word)):
    if word[i] == '_':
        underba.append(i)
    elif word[i] == 'L':
        Lyn = True

# underba 변수 인덱스, 빈칸만 완성된 알파벳, L 여부, 만들 수 있는 단어 수
def dfs(idx, w, yn, cnt):
    global answer
    if idx == len(underba):
        if yn:
            answer += cnt
        return

    for alphabet in alphabets:
        w[idx] = alphabet
        if alphabet == '엘':






dfs(0, word, Lyn, 0)




