import sys, math
from collections import defaultdict, Counter as counter
from bisect import bisect, insort

def stdreadline(): return sys.stdin.readline().strip()
def stdreadint(): return int(stdreadline())
def stdreadints(): return map(int, stdreadline().split())
def stdread(): return sys.stdin.read().split()

def trace(x): sys.stderr.write('%s\n' % x)

T = stdreadint()
for t in range(1, T+1):
    W, H, P, Q, N, X, Y, a, b, c, d = stdreadints()
    trace([W, H, P, Q, N, X, Y, a, b, c, d])
    
    trace('W=%s, H=%s' % (W, H))
    trace('P=%s, Q=%s' % (P, Q))
    trace('')

    marked = defaultdict(dict)
    possibles = (H-Q+1) * (W-P+1) 

    trace('possibles=%s' % possibles)

    dps = [(X, Y,)]
    for i in xrange(1, N):
        dp = ((dps[-1][0] * a + dps[-1][1] * b + 1) % W, (dps[-1][0] * c + dps[-1][1] * d + 1) % H)
        dps.append(dp)

    trace('dps.sz=%s' % len(dps))

    dps = list(set(dps))
            
    for x, y in dps:
        if possibles == 0: break

        #trace('x=%s, y=%s' % (x, y))

        for xi in xrange(max(x-P+1, 0), min(x+1, W-P+1)):
            for yi in xrange(max(y-Q+1, 0), min(y+1, H-Q+1)):
                point = (xi, yi,)
                if yi in marked[xi]: break
                possibles -= 1
                marked[xi][yi] = 1
        
    trace('after: %s' % possibles)

    print 'Case #%s: %s' % (t, possibles)
    print ''

    if t == 5: break

