# 만족해야 하는 값을 DFS의 인자로 넘기게 하기
# -> 단백질, 지방,,, 합을 인자로 넘김
import sys
N = int(input())

m = list(map(int, sys.stdin.readline().split()))

ingredient = []
for _ in range(N):
    ingredient.append(list(map(int, sys.stdin.readline().split())))

def dfs():

dfs(0, [0]*5, [])