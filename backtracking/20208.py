# 민트초코우유 좌표로 dfs
# 우유 선택(선택하면 집돌아올 수 있는지 판변 후 선택) -> dfs -> 우유 선택 풀기
# 우유 선택 순서가 영향이 있는가? 단순히 좌표 순으로 우유를 선택해도 되는가?

import sys

N, M, H = map(int, sys.stdin.readline().split())
