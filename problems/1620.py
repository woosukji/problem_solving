# 1620 나는야 포켓몬 마스터 이다솜

f, *S = [*open(0)]
N = int(f.split()[0])
names = [0] + list(map(str.strip, S[:N]))
idxes = {names[i]:str(i) for i in range(len(names))}
print("\n".join([names[int(q)] if ord(q[0])<65 else idxes[q] for q in map(str.strip, S[N:])]))