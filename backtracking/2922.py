# 즐거운 단어 : 모음(A, E, I, O, U) 연속 3번 X, 자음은 연속 3번 X , L 반드시 포함
# 밑줄이 10개 이하 이므로 3^10 으로 완탐
# dfs 넘겨줄 변수 : 전체문자, 밑줄 idx, 여태껏 완성한 단어
# 밑줄에 들어갈 수 있는 알파벳 : L 제외 자음, 모음, L -> dfs 안에 for문에서 사용

word = input()
LYn = False
underba = []

answer = 0
# L, 자음 21, 모음 5
# 밑줄에 쓰일 알파벳으로 L, B(자음대표), A(모음대표)
alphabets = ['L', 'B', 'A']

for i in range(len(word)):
    if word[i] == '_':
        underba.append(i)

# underba 변수 인덱스, 여태껏 완성된 단어, 밑줄에 쓰인 알파벳
def dfs(idx, w, unw):
    global answer
    if idx == len(underba):
        return

    for alphabet in alphabets:
        w[idx] = alphabet








dfs(0, word, Lyn, 0)




