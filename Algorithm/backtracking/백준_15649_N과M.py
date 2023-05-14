'''
1. 아이디어: 백트레킹

2. 시간복잡도: N!(10까지 가능)

3. 자료구조: int(결과값), bool(방문여부)
'''

import sys
input = sys.stdin.readline

N,M = map(int, input().split())
rs = []
chk = [False] * (N+1)

def backTracking(num):
    if num == M:
        print(' '.join(map(str, rs)))
        return
    for i in range(1, N+1):
        if chk[i] == False:
            chk[i] = True
            rs.append(i)
            backTracking(num+1)
            chk[i] = False
            rs.pop()



       

backTracking(0)