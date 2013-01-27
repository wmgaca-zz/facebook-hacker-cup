import sys, collections, re

pattern = re.compile(r'[a-z]')

for test, string in enumerate([line.strip().lower() for line in sys.stdin.readlines()[1:]], start=1):
    chars = collections.defaultdict(int)
    for s in string: 
        if re.match(pattern, s): chars[s] += 1
    count = [x for x in reversed(sorted(chars.values()))]
    result, factor = 0, 26
    for c in count:
        result += c * factor
        factor -= 1
    print 'Case #%s: %s' % (test, result)
