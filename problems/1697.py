# 1697 숨바꼭질

nn, kk = map(int, input().split())

if nn >= kk:
    print(nn-kk)
    quit()
    
if nn != 0:
    mm = len(bin(int(kk/nn)))-3
else:
    mm = len(bin(int(kk)))-3
    
f = lambda m,r: int(r/2**m) if r%2**m == 0 else int(r/2**m) + min(f(m-1,r%2**m), 1+f(m-1,2**m-(r%2**m)))

print(min(mm+f(mm, abs(kk - nn*2**mm)), mm+1+f(mm+1, abs(kk - nn*2**(mm+1)))))


''' wrong solution - should've taken both (mm, mm+1) into accout

nn, kk = map(int, input().split())
if nn == -1:
    quit()

if nn >= kk:
    print(nn-kk)

if nn != 0:
    mm = len(bin(int(kk/nn)))-3
    if kk > nn*3*2**(mm-1):
        mm = mm+1
else:
    mm = len(bin(int(kk)))-3
    if kk > 3*2**(mm-1):
        mm = mm+1

f = lambda m,r: int(r/2**m) if r%2**m == 0 else int(r/2**m) + min(f(m-1,r%2**m), 1+f(m-1,2**m-(r%2**m)))

print(mm+f(mm, abs(kk - nn*2**mm)))

'''

''' short coding trial - 276B

f=lambda m,r,a:int(r/a) if r%a==0 else int(r/a)+min(f(m-1,r%a,a/2),1+f(m-1,a-(r%a),a/2))
h=lambda m,n,k:min(m+f(m,k-n*2**m,2**m),m+1+f(m+1,2*n*2**m-k,2*2**m))
g=lambda n,k:n-k if n>=k else (h(len(bin(int(k/n)))-3,n,k) if n!=0 else 1+g(1,k))
print(g(*map(int,input().split())))

'''


