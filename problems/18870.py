# 18870 μ’ν μμΆ

L = list( map( int, [*open(0)][1].split() ) )
C = sorted(list(set(L)))
I = { C[i] : i for i in range(len(C)) }
print(*[ I[n] for n in L ])