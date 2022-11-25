# 즐거운 단어 : 모음(A, E, I, O, U) 연속 3번 X, 자음은 연속 3번 X , L 반드시 포함
# dfs 넘겨줄 변수 : 밑줄 idx, 여태껏 완성한 단어, L 포함여부
# 밑줄에 들어갈 수 있는 알파벳 : L 제외 자음, 모음, L
from collections import defaultdict

word = input()
underba = []

for i in range(len(word)):
    if word[i] == '_':
        underba.append(word[i])



