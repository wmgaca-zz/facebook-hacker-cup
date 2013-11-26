import sys

def readline(): return sys.stdin.readline().strip()
def readlinesplit(): return readline().split()
def readlineint(): return int(readline())
def readints(): return map(int, readline().split())
def TRACE(x): print x #sys.stderr.write('%s\n' % x)


class Player(object):

    def __init__(self, *args):
        self.name, self.skill, self.height = args
        self.skill = int(self.skill)
        self.height = int(self.height)

    @staticmethod
    def rate(A, B):
        if A.skill > B.skill:
            return -1
        elif B.skill > A.skill:
            return 1
        elif A.height > B.height:
            return -1
        return 1


for t in xrange(1, readlineint() + 1):
    N, M, P = readints()

    players = [Player(*readlinesplit()) for p in xrange(N)]

    a, b = [], []
    for i, p in enumerate(sorted(players, cmp=Player.rate), start=1):
        if i % 2:
            a.append(p)
        else:
            b.append(p)

    a = 2 * (list(reversed(a[:P])) + a[P:])
    b = 2 * (list(reversed(b[:P])) + b[P:])

    la = len(a) / 2
    lb = len(b) / 2

    players = sorted(a[M % la:(M % la) + P] + b[M % lb:(M % lb) + P],
                     key=lambda x: x.name)

    TRACE('Case #%s: %s' % (t, ' '.join(map(lambda x: x.name, players))))
