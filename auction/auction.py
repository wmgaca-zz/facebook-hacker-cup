import sys

def p(string, sz=15):
    string = str(string)
    
    return string + (sz - len(string)) * ' '

def genp(A, Pprev, B, M):
    return ((A * Pprev + B) % M) + 1

def genw(C, Wprev, D, K):
    return ((C * Wprev + D) % K) + 1

def gen(N, P1, W1, M, K, A, B, C, D):
    products = [(P1, W1)]

    for i in (1, 20):
        Pprev, Wprev = products[-1]

        Pcurr = genp(A, Pprev, B, M)
        Wcurr = genw(C, Wprev, D, K)

        print p(Pcurr), p(Wcurr), p(Pcurr - Pprev), p(Wcurr - Wprev)

        products.append((Pcurr, Wcurr,))

    return products

def findpperiod(N, A, P1, B, M):
    Pprev = P1
    values = {P1: 0}
    p = [P1]
    idx = 1
    while idx < N:
    #for idx in xrange(1, N):
        Pcurr = genp(A, p[-1], B, M)
        p.append(Pcurr)
        if Pcurr in values:
            print "Found period from %s-%s" % (values[Pcurr], idx-1)
            return p
        else:
            values[Pcurr] = idx
        idx += 1

    print "Not found :("

def main():
    auctions = [tuple([int(v) for v in x.split()]) for x in sys.stdin.readlines()[1:]]

    print p('Pcurr'), p('Wcurr'), p('Pcurr - Pprev'), p('Wcurr - Wprev')

    for tc, auction in enumerate(auctions[:5]):
        N, P1, W1, M, K, A, B, C, D = auction

        print '\n== TC %s (N=%s, P1=%s, W1=%s, M=%s, K=%s, A=%s, B=%s, C=%s, D=%s\n' % (tc + 1, N, P1, W1, M, K, A, B, C, D)

        #products = gen(N, P1, W1, M, K,
        products = findpperiod(N, A, P1, B, M)
        #print products

        #print products

if __name__ == '__main__':
    main()
