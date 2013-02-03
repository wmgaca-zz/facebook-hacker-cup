import sys, math
from collections import defaultdict, Counter as counter
from bisect import bisect, insort

def stdreadline(): return sys.stdin.readline().strip()
def stdreadint(): return int(stdreadline())
def stdreadints(): return map(int, stdreadline().split())
def stdread(): return sys.stdin.read().split()

def trace(x): sys.stderr.write('%s\n' % x)

MAX = 1000000007

T = stdreadint()
for t in xrange(1, T+1):
    N, K = tuple(stdreadints())
    a = stdreadints()

    a.sort()

    c, result = long(1), a[K-1]
    for x in xrange(K, N):
        c *= x
        c /= x - (K-1)
        c %= MAX
        result += (a[x] * c) % MAX
        result %= MAX

    print 'Case #%s: %s' % (t, result)
