# 2606 바이러스

N = int(input())
G = [ [] for _ in range(N+1) ]
visited = [0]*(N+1)
infect = 0

def add_node(i, j):
  G[i].append(j)
  G[j].append(i)
  return 1

def visit(n):
  global infect
  for m in G[n]:
    if not visited[m]: 
      infect += 1
      visited[m] = 1
      visit(m)

_ = [ add_node(*map(int,input().split())) for _ in range(int(input())) ]

visited[1] = 1
visit(1)

print(infect)