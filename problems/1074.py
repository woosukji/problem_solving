# 1074 Z

f = lambda m,r,c: 0 if m<1 else (r>=m) * m**2 * 2 + (c>=m) * m**2 + f(m/2, r%m, c%m)
n,r,c = map(int, input().split())
print(int(f(2**n//2,r,c)))
