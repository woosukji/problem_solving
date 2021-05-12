for i in range(100):
    nn, kk = map(int, input().split())
    if nn == -1:
        quit()

    if nn >= kk:
        print(nn-kk)
        continue
        
    if nn != 0:
        mm = len(bin(int(kk/nn)))-3
        if kk > nn*3*2**(mm-1):
            mm = mm+1
    else :
        mm = len(bin(int(kk)))-3
        if kk > 3*2**(mm-1):
            mm = mm+1

    f = lambda m,r: int(r/2**m) if r%2**m == 0 else int(r/2**m) + min(f(m-1,r%2**m), 1+f(m-1,2**m-(r%2**m)))

    print(mm+f(mm, abs(kk - nn*2**mm)))

    