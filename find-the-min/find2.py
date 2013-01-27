import sys
from time import gmtime, strftime
from collections import defaultdict

def stdreadline(): return sys.stdin.readline().strip()
def stdreadint(): return int(stdreadline())
def stdreadints(): return tuple(map(lambda x: int(x.strip()), stdreadline().split()))

def gen(a, b, c, r, k):
    m = [a]
    used = defaultdict(int)
    used[a] = 1

    for i in xrange(1, k):
        val = (b * m[-1] + c) % r
        m.append(val)
        used[val] += 1
    return m, used

def insert(sortedlist, value):
    if value < sortedlist[0]:
        sortedlist.insert(0, value)
        return
    if value > sortedlist[-1]:
        sortedlist.append(value)
        return

    for i in xrange(len(sortedlist)):
        if i < sortedlist[i]:
            sortedlist.insert(i, value)
            inserted = True
            return

    print 'This should never happen'
    sys.exit()

print 'start: %s' % strftime("%Y-%m-%d %H:%M:%S", gmtime())

for t in xrange(1, stdreadint() + 1):
    
    n, k = stdreadints()
    a, b, c, r = stdreadints()    

    m, used = gen(a, b, c, r, k)
    
    unused = [x for x in xrange(2*k) if x not in used]

    m.append(unused[0])
    used[unused[0]] = 1
    unused.pop(0)
    
    last = len(m) - 1

    limit = 2*k
    print limit

    while last != limit:
        currval = m[0]

        if not len(unused): 
            print n, k
            print 'Big bad error'
            sys.exit()
        
        if used[currval] == 0:
            if currval < unused[0]:
                m.append(currval)
                used[currval] = 1
            else:
                m.append(unused[0])
                used[unused[0]] = 1
                unused.pop(0)

                insert(unused, currval)

        elif used[currval] > 1:
            used[currval] -= 1
            m.append(unused[0])
            unused.pop(0)
        elif used[currval] == 1:
            if currval < unused[0]:
                m.append(currval)
            else:
                used[currval] = 0
                m.append(unused[0])
                used[unused[0]] = 1
                unused.pop(0)

                insert(unused, currval)

        m.pop(0)
        last += 1

    print strftime("%Y-%m-%d %H:%M:%S", gmtime())
    print 'Case #%s:' % t
    print 'n=%s, k=%s, last=%s' % (n, k, last)
    print '----'
    continue

    try:
        print m[n-1]
    except IndexError:
        print 'There is more.'

print strftime("%Y-%m-%d %H:%M:%S", gmtime())
