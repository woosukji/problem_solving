# 9095 1,2,3 더하기

f=lambda x:0**x or x*f(x-1)
g=lambda k:sum([ f(x+y+z)//(f(x)*f(y)*f(z)) for z in range(k//3+1) for y in range((k-3*z)//2+1) for x in [k-3*z-2*y] ])
[print(g(int(input()))) for _ in range(int(input()))]