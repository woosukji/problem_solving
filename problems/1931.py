# 1931 회의실 배정

import sys

T = [ list(map(int, input().split())) for _ in range(int(input())) ]
T = sorted( T, key=lambda x: (x[1], x[0]) )

start = 0
end = T[0][1]
acc = 0

for a in T:
    
  if end < a[1]:
    end = a[1]
    
  if start <= a[0]:
    start = end
    acc += 1
    
print(acc)

''' 
# wrong - misunderstand step iteration

def f(T):
  if len(T)==0: return 0
  m = min([c[1] for c in T])
  TT = [a for a in T if a[0]>m or a[1]>a[0]>=m]
  return 1+f(TT)+T.count([m,m])                        # prob: over counts for [m,m]
print(f(T))

'''

''' 
# memory over - reassigning big array for each recursion stack

def f(T):
  if len(T)==0: return 0
  m = min([c[1] for c in T])
  TTT = [a for a in T if a[1]<=m]
  c = TTT.count([m,m])
  return f([a for a in T if a[0]>m or a[1]>a[0]>=m])+c+(c<len(TTT))
print(f(T))

'''

''' 
# time over - when modified to use 'while'. since O(n^2)

T = sorted(T, key=lambda x:x[1])
acc = 0
while len(T) > 0:
  c = 0
  m = T[0][1]
  while c < len(T) and T[c][1] == m: c += 1
  ms = T[0:c].count([m,m])
  acc += ms + (ms < c)
  T = list(filter(lambda x: x[0]>=m and x[1]>m, T[c:]))    # prob: skimming through entire T
print(acc)

'''