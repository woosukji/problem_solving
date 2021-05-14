# 1012 유기농 배추

from collections import deque


def visit(m,n) :
    
  q.append((m,n))

  while len(q) > 0:
        
    x,y = q.popleft()
    
    if not visited[x][y]:
        
      visited[x][y] = 1
    
      if x<M-1 and field[x+1][y] and not visited[x+1][y] : q.append((x+1,y))
      if y<N-1 and field[x][y+1] and not visited[x][y+1] : q.append((x,y+1))
      if x>0 and field[x-1][y] and not visited[x-1][y] : q.append((x-1,y))
      if y>0 and field[x][y-1] and not visited[x][y-1] : q.append((x,y-1))

        
for i in range(int(input())) :
    
  M,N,K = map(int,input().split())

  field = [[0]*N for _ in range(M)]
  visited = [[0]*N for _ in range(M)]
  B = 0
  q = deque([])

  for j in range(K) :
    m,n = map(int,input().split())
    field[m][n] = 1
  for m in range(M) :
    for n in range(N) :
      if field[m][n] and not visited[m][n] :
        B += 1
        visit(m,n)
  print(B)


''' wrong - repetedly assigning object acts as copying

  field = [[0]*N]*M
  visited = [[0]*N]*M

'''

''' timeout - queueing same points repetedly (inevitable, so must check when popped)

def visit(m,n) :
  q.append((m,n))
  while len(q) > 0:
    x,y = q.popleft()
    visited[x][y] = 1
    if x<M-1 and field[x+1][y] and not visited[x+1][y] : q.append((x+1,y))
    if y<N-1 and field[x][y+1] and not visited[x][y+1] : q.append((x,y+1))
    if x>0 and field[x-1][y] and not visited[x-1][y] : q.append((x-1,y))
    if y>0 and field[x][y-1] and not visited[x][y-1] : q.append((x,y-1))

'''