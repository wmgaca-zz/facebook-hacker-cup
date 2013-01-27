import sys
def stdreadline(): return sys.stdin.readline().strip()
def stdreadint(): return int(stdreadline())
def stdreadints(): return tuple(map(lambda x: int(x.strip()), stdreadline().split()))


def gen(a, b, c, r, k):
    m = [a]
    for i in xrange(1, k):
        m.append((b*m[-1]+c)%r)
    return m

def add(m, window, swindow, x):
    m.append(x)

    swindow.remove(window.pop(0))
    swindow.append(x)
    swindow.sort()

    window.append(x)

def findmin(sortedlist):
    '''Bisect for the lowest value not present in the sorted list.
    '''

    sortedlist = list(set(sortedlist))
    sortedlist.sort()

    if sortedlist[-1] == len(sortedlist) - 1: return sortedlist[-1] + 1
    if sortedlist[0] != 0: return 0

    a, b = 0, len(sortedlist) - 1
    while abs(a-b) > 1:
        c = (a+b) / 2
        #print a, b, c, sortedlist[c]
        if sortedlist[c] == c: a = c
        else: b = c 
    return sortedlist[a] + 1

T = stdreadint()
for t in xrange(1, T+1):
    n, k = stdreadints()
    a, b, c, r = stdreadints()

    
    #if t != 2: continue

    m = gen(a, b, c, r, k)

    #print 'm: %s' % m

    window = m[-1*k:]
    swindow = window[-1*k:]
    swindow.sort()

    #print 'w: %s' % window
    #print 's: %s' % swindow

    while len(m) < n:
        x = findmin(swindow)
        #print swindow
        #print 'add: %s' % x
        

        todel = window.pop(0)

        #print 'del: %s' % todel

        window.append(x)

        m.append(x)

        swindow.remove(todel)
        swindow.append(x)
        swindow.sort()

        #print window
        #print '------------------'  
    
        '''
        for x in swindow:
            if swindow.count(x) > 1:
                print 'Big bad error'
                sys.exit()
        '''
    
    #print "k=%s, n=%s, len(window)=%s, len(m)=%s" % (k, n, len(window), len(m))
    #print "%s" % window
    #print '%s' % m[-1*k:]

    print "Case #%s: %s" % (t, m[n-1])
    #break
