import sys, math
from collections import defaultdict, Counter as counter
from bisect import bisect, insort

def stdreadline(): return sys.stdin.readline().strip()
def stdreadint(): return int(stdreadline())
def stdreadints(): return map(int, stdreadline().split())
def stdread(): return sys.stdin.read().split()

def trace(x): sys.stderr.write('%s\n' % x)

def statehash(pegs):
    global hashmem
    pegs = tuple([tuple(peg) for peg in pegs])
    if tuple(pegs) in hashmem: 
        return hashmem[pegs]
    result = '|'.join(['.'.join([str(p) for p in peg]) for peg in pegs])
    hashmem[pegs] = result
    return result

def solve(state, moves):
    global minmoves, mem
    if len(moves) > 6 or len(moves) > minmoves: return

    h = statehash(state)

    if h == fhash: 
        mem[len(moves)].append(moves)
        if len(moves) < minmoves: minmoves = len(moves)
        return

    for i, s in enumerate(state):
        if not len(s): continue
        for j, n in enumerate(state):
            if i == j: continue
            if len(n):
                if n[0] < s[0]: continue
            newstate = [list(ss) for ss in state]
            newstate[j].insert(0, newstate[i].pop(0))
            solve(newstate, moves + [(i+1, j+1,)])

N, K = stdreadints()
start, final = stdreadints(), stdreadints()

global minmoves, hashmem, mem, fhash
minmoves = 7
hashmem = {}
mem = defaultdict(list)

pegs = [[] for x in range(K)]
for i, x in enumerate(start): pegs[x-1].append(i+1)

fpegs = [[] for x in range(K)]
for i, x in enumerate(final): fpegs[x-1].append(i+1)

fhash = statehash(fpegs)

solve(list(pegs), [])

for pair in mem[minmoves][0]:
    print '%s %s' % pair
