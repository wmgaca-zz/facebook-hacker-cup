from sys import stdin
tokens = stdin.read().split()
N = int(tokens.pop(0))
for n in range(1, N + 1):
    M, S = int(tokens.pop(0)), tokens.pop(0)
    L = len(S)
    C = [0]*L + [1]
    for i in reversed(range(L)):
        if S[i] == '0':
            continue
        for j in range(i + 1, L + 1):
            if int(S[i:j]) > M:
                break
            C[i] += C[j]
        C[i] %= 0xfaceb00c
    print('Case #%d: %d'%(n, C[0]))
