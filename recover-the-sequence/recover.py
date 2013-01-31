import sys, math
from collections import defaultdict, Counter as counter
from bisect import bisect, insort

def stdreadline(): return sys.stdin.readline().strip()
def stdreadint(): return int(stdreadline())
def stdreadints(): return map(int, stdreadline().split())

def trace(x): sys.stderr.write('%s\n' % x)

def checksum(arr):
    result = 1
    for i in xrange(len(arr)): 
        result = (31 * result + arr[i]) % 1000003
    return result

def merge(a, b):
    global debug
    result = []
    while len(a) > 0 and len(b) > 0:
        if debug[0] == '1': 
            result.append(a.pop(0))
        else: result.append(b.pop(0))
        debug = debug[1:]
    result.extend(a)
    result.extend(b)
    return result

def merge_sort(data):
    n = len(data)
    if n <= 1: return data
    mid = int(math.floor(n // 2))
    return merge(merge_sort(data[:mid]), merge_sort(data[mid:]))

for t in xrange(1, stdreadint() + 1):
    global debug

    N, debug = stdreadint(), stdreadline()
    data = range(1, N+1)

    for i, x in enumerate(merge_sort(data), start=1):
        data[x-1] = i

    print 'Case #%s: %s' % (t, checksum(data))
