# 즐거운 단어 : 모음(A, E, I, O, U) 연속 3번 X, 자음은 연속 3번 X , L 반드시 포함
# dfs 넘겨줄 변수 : 밑줄 idx, 여태껏 완성한 단어, L 포함여부, 가능 단어 개수
# 밑줄에 들어갈 수 있는 알파벳 : L 제외 자음, 모음, L -> dfs 안에 for문에서 사용
from collections import defaultdict

word = input()
LYn = False
underba = []
answer = 0
# L, 자음 21, 모음 5
alphabet_visited = defaultdict(int)
alphabet_visited['L'] = 0
alphabet_visited['B'] = 0
alphabet_visited['A'] = 0

for i in range(len(word)):
    if word[i] == '_':
        underba.append(word[i])
    elif word[i] == 'L':
        Lyn = True

def dfs(idx, w, yn, cnt):
    global answer
    if idx == len(underba):
        answer += cnt
        return



dfs(0, word, Lyn, 0)




