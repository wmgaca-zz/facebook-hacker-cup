import sys
import bisect
from collections import defaultdict
from time import gmtime, strftime

def stdreadline(): return sys.stdin.readline().strip()
def stdreadint(): return int(stdreadline())
def stdreadints(): return tuple(map(lambda x: int(x.strip()), stdreadline().split()))

def gen(a, b, c, r, k):
    global m, used

    m = [a]
    used = defaultdict(int)
    used[a] = 1
    val = a
    for i in xrange(1, k):
        val = (b * val + c) % r
        m.append(val)
        used[val] += 1

def addunused():
    global m, unused, used    
    m.append(unused[0])
    used[unused[0]] += 1
    unused.pop(0)
    unused.append(unused[-1] + 1)

def addvalue(value):
    global m, unused, used
    m.append(value)
    used[value] += 1

for t in xrange(1, stdreadint() + 1):
    n, k = stdreadints()
    a, b, c, r = stdreadints()

    global m, used, unused

    gen(a, b, c, r, k)
    unused = [x for x in xrange(2*k+1) if x not in used]

    addunused()

    for i in xrange(0, len(m)):
        curr = m[i]
        used[curr] -= 1

        if used[curr] > 0:
            addunused()
        elif curr < unused[0]:  
            addvalue(curr)
        elif curr > unused[0]:
            addunused()
            if curr <= k: bisect.insort(unused, curr)
    
    m.append(m[k])
    res = n % (k+1)

    print 'Case #%s: %s' % (t, m[-1*(k+1)-2+res])

