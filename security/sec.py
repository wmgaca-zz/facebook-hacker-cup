import sys, math
from collections import defaultdict, Counter as counter
from bisect import bisect, insort

def stdreadline(): return sys.stdin.readline().strip()
def stdreadint(): return int(stdreadline())
def stdreadints(): return map(int, stdreadline().split())
def stdread(): return sys.stdin.read().split()

def trace(x): sys.stderr.write('%s\n' % x)

def comparekeys(a, b):
    global mem
    aplusb = a+b
    if aplusb in mem: return mem[aplusb]

    result = True
    for la, lb in zip(a, b):
        if '?' in [la, lb] or la == lb: continue
        else:
            result = False
            break

    mem[aplusb] = result
    mem[b+a] = result
    return result

def solve(key, possibles, current):
    if not key: return [current.replace('?', 'a')]
    
    if possibles[key[0]]:
        new_possibles = possibles.copy()
        new_possibles[key[0]] -= 1
        return solve(key[1:], new_possibles, current+key[0])

    keys = []
    for k in sorted(possibles.keys()):
        v = possibles[k]
        if v:
            if comparekeys(key[0], k):
                new_possibles = possibles.copy()
                new_possibles[k] -= 1
                keys = solve(key[1:], new_possibles, current+key[0])
                if keys: break
    keys.sort()

    return keys[:1]

T = stdreadint()
for t in xrange(1, T+1):
    global mem
    mem = {}

    m, k1, k2 = stdreadint(), stdreadline(), stdreadline()
    l = len(k1)
    ml = l/m

    p = []
    key, possibles = [], defaultdict(int)
    for x in xrange(m):
        start, end = x*ml, (x+1)*ml
        key.append(k1[start:end])
        possibles[k2[start:end]] += 1
        p.append(k2[start:end])

    if k1.count('?') == l:
        possibles = [x.replace('?', 'a') for x in p]
        possibles.sort()
        key = ''.join(possibles)
    elif k2.count('?') == l:
        key = k1.replace('?', 'a')
    else: 
        key = solve(list(key), possibles.copy(), current='')
        if not key: key = 'IMPOSSIBLE'
        else: key = key[0]

    print 'Case #%s: %s' % (t, key)
