# 1927 최소 힙

H = []

def push(n):
    
    H.append(n)
    cursor = len(H)

    while cursor > 1 and H[cursor//2 - 1] > n:
        H[cursor - 1] = H[cursor//2 - 1]
        cursor //= 2

    H[cursor - 1] = n


def pop():

    if len(H) == 0: return 0

    minimum, n, cursor = H[0], H.pop(), 1

    if len(H) == 0: return minimum

    while cursor*2 <= len(H) and n > min(H[cursor*2 - 1 : cursor*2 + 1]):
        smaller = cursor*2 if cursor*2 == len(H) or H[cursor*2 - 1] < H[cursor*2] else cursor*2 + 1
        H[cursor - 1], cursor = H[smaller - 1], smaller

    H[cursor - 1] = n
    return minimum


for n in [*open(0)][1:]:
    n = int(n[:-1])
    if n == 0: print(pop())
    else: push(n)


'''
# short coding trial - 110B

from heapq import*
H=[];[heappush(H,int(n))if int(n) else print(heappop(H)if H else 0)for n in [*open(0)][1:]]

'''