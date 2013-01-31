import sys, math
from collections import defaultdict, Counter as counter
from bisect import bisect, insort

def stdreadline(): return sys.stdin.readline().strip()
def stdreadint(): return int(stdreadline())
def stdreadints(): return map(int, stdreadline().split())
def stdread(): return sys.stdin.read().split()

def trace(x): sys.stderr.write('%s\n' % x)

def digits(number): return int(math.log10(number)) + 1

MOD = 4207849484

def count(start):
    if start > last: return 1
    if not m[start]: return 0
    if start in mem: return mem[start]

    mem[start] = 0
    for number in m[start]:
        mem[start] += count(start+digits(number))

    mem[start] %= MOD

    return mem[start]

def solve(N, status):
    if status.startswith('0'): return 0

    global m, last, mem

    l = len(N)
    N = int(N)

    mem = {}
    last = len(status) - 1
    m = defaultdict(list)

    for start, char in enumerate(status):
        if char == '0': continue
        for end in xrange(start+1, min(start+l, len(status))+1):
            number = int(status[start:end])
            if number <= N: m[start].append(number)
            else: break
    
    return count(0)

data = stdread()
T = int(data.pop(0))

for t in range(1, T+1):
    N = data.pop(0)
    status = data.pop(0)

    print 'Case #%s: %s' % (t, solve(N, status))
