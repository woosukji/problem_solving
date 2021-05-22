# 7576 토마토

from collections import deque

M,N = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(N)]

ripen = [ (i,j) for i in range(N) for j in range(M) if G[i][j] == 1 ]
q = deque(ripen)

def search(i,j):
    for di,dj in zip([0,1,0,-1], [1,0,-1,0]):
        if 0 <= i+di < N and 0 <= j+dj < M and G[i+di][j+dj] == 0:
            G[i+di][j+dj] = 1
            q.appendleft((i+di,j+dj))

D = -1
l = len(q)
while l > 0:
    for _ in range(l):
        search(*q.pop())
    D += 1
    l = len(q)
    
if len([0 for i in range(N) for j in range(M) if G[i][j] == 0]) > 0:
    print(-1)
else:
    print(D)
