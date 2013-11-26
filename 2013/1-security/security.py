import sys, math
from collections import defaultdict, Counter as counter
from bisect import bisect, insort

def stdreadline(): return sys.stdin.readline().strip()
def stdreadint(): return int(stdreadline())
def stdreadints(): return map(int, stdreadline().split())
def stdread(): return sys.stdin.read().split()

def trace(x): sys.stderr.write('%s\n' % x)

cmpmem = {}

def cmpkeys(a, b):
    global cmpmem
    if (a, b) in mem: return mem[(a, b)]

    for la, lb in zip(a, b):
        if la == '?' or lb == '?': continue
        if la == lb: continue
        else:
            cmpmem[(a, b)] = False
            return False
    cmpmem[(a, b)] = True
    return True

def solve(key, possibles, current):
    global mem

    if current == len(key): return [''.join(key).replace('?', 'a')]
    if not mem[current]: return []

    keys = []
    new_key = list(key)

    trace('len = %s, curr = %s' % (len(mem[current]), current))

    for possible in mem[current]:
        if possible not in possibles: continue
        if key[current].count('?') > 0: new_key[current] = possible.replace('?', 'a')
        new_possibles = list(possibles)
        new_possibles.remove(possible)
        keys.extend(solve(new_key, new_possibles, current+1))

    keys.sort()

    if not keys: return []
    else: return keys[:1]
    
T = stdreadint()
for t in xrange(1, T+1):
    global mem

    m, k1, k2 = stdreadint(), stdreadline(), stdreadline()
    l = len(k1)
    modlen = l/m 

    key = []

    for x in xrange(m):
        start, end = x * modlen, (x+1) * modlen
        key.append(k1[start:end])

    mem, possibles = defaultdict(list), []
    for x in xrange(m):
        start, end = x * modlen, (x+1) * modlen
        sub = k2[start:end]
        found = False
        for i, k in enumerate(key): 
            if cmpkeys(k, sub): 
                mem[i].append(sub)
                found = True
        if found: possibles.append(sub)
 
    key = solve(list(key), list(possibles), current=0)

    if not key: key = 'IMPOSSIBLE'
    else: key = key[0]
    
    print 'Case #%s: %s' % (t, key)
