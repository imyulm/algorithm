# antic 최소 5글자 이상은 가르쳐야함
# antic 아닌 글자 뭐 있는지 목록 작성
# antic 아닌 글자들 뭐뭐 있는지 각 단어마다 리스트에 넣어줌
# 시간초과 -> deepcopy, set으로 dfs
# alphabet을 key로 하는 dict 만들어서 선택됐는지 안됐는지

import sys
from collections import defaultdict

answer = 0
N, K = map(int, sys.stdin.readline().split())
# antic 제외 글자 저장
letter_without_5 = set()
# antic 글자 저장
letter_with_5 = set(['a','n','t','i','c'])
# antic 제외하고 각 단어에 어떤 글자 있는지 저장
word = []
# antic 제외하고 몇 개 글자 더 선택할 수 있는가
learn_more_letter = K - 5

learn = defaultdict(int)

for i in range(N):
    tmp_letter = str(input())
    tmp_letter = set(tmp_letter[4:-4])
    tmp_letter = set(tmp_letter) - set(letter_with_5)
    word.append(tmp_letter)
    letter_without_5.update(tmp_letter)
letter_without_5 = list(letter_without_5)
word = list(word)

def getMaxWords():
    sum = 0
    tmp_words = word[:]
    for tmp_word in tmp_words:
        check = True
        for w in tmp_word:
            if not learn[w]:
                check = False
        if check:
            sum += 1
    return sum

def selectAlphabet(idx, cnt):
    global answer
    if cnt == learn_more_letter:
        answer = max(answer, getMaxWords())
        return

    for i in range(idx, len(letter_without_5)):
        learn[letter_without_5[i]] = 1
        selectAlphabet(i+1, cnt+1)
        learn[letter_without_5[i]] = 0


if learn_more_letter < 0:
    print(0)
elif learn_more_letter == 21:
    print(N)
else:
    selectAlphabet(0, 0)
    print(answer)

