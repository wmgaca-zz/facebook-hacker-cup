import sys, math
from collections import defaultdict, Counter as counter
from bisect import bisect, insort

def stdreadline(): return sys.stdin.readline().strip()
def stdreadint(): return int(stdreadline())
def stdreadints(): return map(int, stdreadline().split())

def trace(x): sys.stderr.write('%s\n' % x)

def d(start, end):
    if start == end: return 0
    if (start, end) in mem: return mem[(start, end)]

    sl = x[start:end+1]
    if len(sl) == 1: 
        mem[(start, end)] = 0
        return 0
    
    counts = []
    for i in xrange(sl[0], sl[-1]+1):
        count = 0
        for o in sl: count += abs(i - o)
        counts.append(count)
    count = min(counts)
    mem[(start, end)] = count
    return count

def solve(start, end, k, count):
    global smem, mincount

    if mincount is not None:
        if count > mincount: return None

    if (start, end, k) in smem: return smem[(start, end, k)]

    if k == 1: 
        ret = d(start, end)
        smem[(start, end, k)] = ret
        if mincount is None: mincount = count + ret
        elif mincount > count+ret: mincount = count+ret
        return ret
    
    if k > end-start+1: 
        smem[(start, end, k)] = None
        return None
    
    counts = []
    for newstart in xrange(start+1, end+1):
        myd = d(start, newstart-1)
        c = solve(newstart, end, k-1, count+myd)
        if c is None: continue
        counts.append(c + myd)
    ret = min(counts) if counts else None
    smem[(start, end, k)] = ret
    
    return ret 
    
T = stdreadint()
for t in xrange(T):
    global N, K, x, mem, smem, mincount
    mincount = None
    mem = {}
    smem = {}
    N, K = stdreadints()
    x = stdreadints()
    x.sort()
    
    if len(set(x)) <= K: print '0'
    else: print '%s' % solve(0, N-1, K, 0)
