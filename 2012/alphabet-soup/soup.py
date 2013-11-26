import sys
from collections import defaultdict

def main():
    lines = sys.stdin.readlines()

    for tc, line in enumerate(lines[1:]):
        occurences = defaultdict(int)
    
        for char in line:
            occurences[char] += 1
        occurences['C'] /= 2
        
        print 'Case #%s: %s' % (tc + 1, min([occurences[x] for x in "HACKERUP"]))

if __name__ == '__main__':
    main()
