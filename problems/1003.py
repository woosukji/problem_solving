# 1003 피보나치 함수

c = {}
def f(n):
    if n==0: return (1,0)
    if n==1: return (0,1)
    if n in c: return c[n]
    c[n] = (f(n-1)[0]+f(n-2)[0], f(n-1)[1]+f(n-2)[1])
    return c[n]

for i in range(int(input())) :
    a = f(int(input()))
    print(f'{a[0]} {a[1]}')