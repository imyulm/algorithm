# antic 최소 5글자 이상은 가르쳐야함
# antic 아닌 글자 뭐 있는지 목록 작성
# antic 아닌 글자들 뭐뭐 있는지 각 단어마다 리스트에 넣어줌
# 시간초과 -> deepcopy, set으로 dfs
# 시간초과 해결 : alphabet을 key로 하는 dict 만들어서 선택됐는지 안됐는지
# 반례 : 각 단어에서 antic 제외하고 남는 문자가 antic제외하고 더 가르칠 수 있는 문자 개수보다 작을 때
# 2 7
# antatica
# antaktica
# 각 단어에서 antic말고 새로운 글자는 k 뿐인데 더 가르칠 수 있는 문자는 2개

import sys
from collections import defaultdict

answer = 0
N, K = map(int, sys.stdin.readline().split())
# antic 제외하고 몇 개 글자 더 선택할 수 있는가
learn_more_letter = K - 5

if learn_more_letter < 0:
    print(0)
    exit()
elif learn_more_letter == 21:
    print(N)
    exit()

# antic 제외 글자 저장
letter_without_5 = set()
# antic 글자 저장
letter_with_5 = set(['a','n','t','i','c'])
# antic 제외하고 각 단어에 어떤 글자 있는지 저장
word = []


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
    for tmp_word in word:
        check = True
        for w in tmp_word:
            if not learn[w]:
                check = False
        if check:
            sum += 1
    return sum

def selectAlphabet(idx, cnt):
    global answer
    # or 후자 조건으로 반례 해결
    if cnt == learn_more_letter or (learn_more_letter > len(letter_without_5) == cnt):
        answer = max(answer, getMaxWords())
        return

    for i in range(idx, len(letter_without_5)):
        learn[letter_without_5[i]] = 1
        selectAlphabet(i+1, cnt+1)
        learn[letter_without_5[i]] = 0



selectAlphabet(0, 0)
print(answer)

