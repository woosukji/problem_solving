# 2630 색종이 만들기

P = [ list(map(int, input().split())) for _ in range(int(input())) ]
slicing = lambda P,vs,ve,hs,he: [ P[v][hs:he] for v in range(vs,ve) ]
papers = [0,0]

def f(P):

N = len(P)

for i in range(N):
    for j in range(N):

        if P[i][j] != P[0][0]:

            n = N//2
            f(slicing(P,0,n,0,n))
            f(slicing(P,0,n,n,N))
            f(slicing(P,n,N,0,n))
            f(slicing(P,n,N,n,N))
            return

    papers[P[0][0]] += 1


f(P)
for p in papers:
    print(p)


'''
# short coding trial - 266B

p=[0,0]
def f(P):
    N=len(P)
    if (not P[0][0]) in [_ for a in P for _ in a]:n=N//2;X=(0,n),(n,N);return [f([P[o][e:r] for o in range(q,w)]) for q,w in X for e,r in X]
    p[P[0][0]]+=1
f([list(map(int,input().split())) for _ in range(int(input()))])
set(map(print,p))

'''