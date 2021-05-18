# 1764 듣보잡

N,M = map(int,input().split())
D = sorted([input() for _ in range(N)])
B = sorted([input() for _ in range(M)])
DB = []

n = i = j = 0
while i<N and j<M:
    while i<N and j<M and D[i]<B[j]: i+=1
    if i<N and j<M and D[i]==B[j]:
        n+=1
        DB.append(D[i])
        i+=1
        j+=1
    else:
        while i<N and j<M and D[i]>B[j]: j+=1
print(n)
for db in DB:
      print(db)