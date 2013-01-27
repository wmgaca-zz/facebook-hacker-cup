import sys

def validate(stack):
    state = 0
    for s in stack:
        if state < 0: return False
        if s == '(':
            state += 1
        elif s == ')':
            state -= 1
    return 0 == state

def solve(string, stack=''):
    if not string: return validate(stack)

    if string[:2] in [':)', ':(']:
        return solve(string[2:], stack + string[1]) or solve(string[2:], stack)
    elif string[0] in '()':
        return solve(string[1:], stack + string[0])
    else:
        return solve(string[1:], stack)

for test, line in enumerate((x.strip() for x in sys.stdin.readlines()[1:]), start=1):
    print "Case #%s: %s" % (test, 'YES' if solve(line) else 'NO')
