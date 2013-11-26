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
    #trace([W, H, P, Q, N, X, Y, a, b, c, d])
       
    possibles = (H-Q+1) * (W-P+1)

    dps, last = set([(X, Y,)]), [X, Y]
    for i in xrange(1, N):
        last = ((last[0] * a + last[1] * b + 1) % W, (last[0] * c + last[1] * d + 1) % H)
        dps.add(last)
        
    dps = sorted(list(dps))

    mindx = 2*P-1
    mindy = 2*Q-1

    done = set()
    for index, dp in enumerate(dps):
        if possibles == 0: break

        x, y = dp
        dead = (min(x+1, W-P+1) - max(x-P+1, 0)) * (min(y+1, H-Q+1) - max(y-Q+1, 0))

        for dp2 in done:
            dx, dy = abs(dp2[0] - dp[0]), abs(dp2[1] - dp[1])
            if dx < mindx and dy < mindy: dead -= abs(mindx-dx) * abs(mindy-dy)

        possibles -= dead
        done.add(dp)

    print 'Case #%s: %s' % (t, possibles)
