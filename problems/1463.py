# 1463 1로 만들기

c = [0, 0, 1, 1]

def f(x):
    if x<3:
        return c[x]
    return min(1 + x%3 + f(x//3), 1 + x%2 + f(x//2))

print(f(int(input())))


''' recursion depth error - naively put x-1 calc to recursion

i=10**6
c=[-1,0,1,1]+[-1]*i
def f(x):
  if x%1!=0:return i
  if c[int(x)]>=0:return c[int(x)]
  c[int(x)]=1+min(f(x/3),f(x/2),f(x-1))
  return c[int(x)]
print(int(f(int(input()))))

'''

''' short coding trial - 91B

f=lambda x:[0,0,1,1][x] if x<3 else min(1+x%3+f(x//3),1+x%2+f(x//2))
print(f(int(input())))

'''