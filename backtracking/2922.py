# 즐거운 단어 : 모음(A, E, I, O, U) 연속 3번 X, 자음은 연속 3번 X , L 반드시 포함
# 밑줄이 10개 이하 이므로 3^10 으로 완탐 -> dfs 변수에 L포함인지, 개수 몇개인지 인자로 들고 다닐 필요 x 일단 단어 완성시키고 판별가능
# dfs 넘겨줄 변수 : 전체문자, 밑줄 idx, 여태껏 완성한 단어
# 밑줄에 들어갈 수 있는 알파벳 : L 제외 자음, 모음, L -> dfs 안에 for문에서 사용

word = input()
LYn = False
underba = []

answer = 0
# L, 자음 21, 모음 5
# 밑줄에 쓰일 알파벳으로 L, B(자음대표), A(모음대표)
alphabets = ['L', 'B', 'A']
vowel = ['A','E','I','O','U']


for i in range(len(word)):
    if word[i] == '_':
        underba.append(i)

def answerYn(answer_word):
    # L 있는가
    if 'L' not in answer_word:
        return False
    # 자음, 모음 연속 3번 x
    cons_num = 0
    vowel_num = 0
    for i in range(len(answer_word)):
        if vowel_num == 3 or cons_num == 3:
            return False
        if answer_word[i] in vowel:
            vowel_num += 1
            cons_num = 0
        else:
            cons_num += 1
            vowel_num = 0

    return True

# underba 변수 인덱스, 여태껏 완성된 단어, 밑줄에 쓰인 알파벳
def dfs(idx, w, unw):
    global answer
    if idx == len(underba):
        if answerYn(w):

        return

    for alphabet in alphabets:
        w[idx] = alphabet
        unw.append(alphabet)
        dfs(idx+1, w, unw)
        w[idx] = '_'
        unw.pop()






dfs(0, word, [])




