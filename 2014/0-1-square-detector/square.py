import sys
import re

def readline(): return sys.stdin.readline().strip()
def readlineint(): return int(readline())
def readints(): return map(int, readline().split())


PATTERN = re.compile(r'^\.*#+\.*$')


def check_line(line):
    return re.match(PATTERN, line) is not None


def detect(data):
    state = 0
    size = 0
    actual_size = 0

    for index, line in enumerate(data):
        if state == 0 and '#' in line:
            if not check_line(line):
                return False
            state = 1
            size = line.count('#')
            actual_size = 1
        elif state == 1 and '#' in line:
            if line != data[index-1]:
                return False
            actual_size += 1
            if actual_size > size:
                return False
        elif state == 1:
            if actual_size != size:
                return False
            state = 2
        elif state == 2 and '#' in line:
            return False

    if state == 0:
        return False

    if size != actual_size:
        return False

    return True


for t in xrange(1, readlineint() + 1):
    data = [readline() for n in xrange(readlineint())]

    result = detect(data)

    print 'Case #%d: %s' % (t, 'YES' if result else 'NO')
