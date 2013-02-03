import sys, math
from collections import defaultdict, Counter as counter
from bisect import bisect, insort

def stdreadline(): return sys.stdin.readline().strip()
def stdreadint(): return int(stdreadline())
def stdreadints(): return map(int, stdreadline().split())
def stdread(): return sys.stdin.read().split()

def trace(x): sys.stderr.write('%s\n' % x)


number = [x for x in sys.argv[1]]

trace(number)
zero = None

for i, x in enumerate(number):
    if x == '0' and zero is None: 
        trace('zero = %s' % i)
        zero = i
    elif zero is not None: 
        trace('zero! %s %s' % (i, zero))
        number[i], number[zero] = '0', x
        zero = i
    trace(number)
trace(number)

