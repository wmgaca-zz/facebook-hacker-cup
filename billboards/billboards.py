import sys

def width(line, fsize):
    return fsize * len(line)

def height(lines, fsize):
    return len(lines) * fsize

def main():
    testcases = sys.stdin.readlines()

    for tc, line in enumerate(testcases[1:]):
        tokens = line.split()
        w, h = [int(x) for x in tokens[:2]]
        words = tokens[2:]

        fsize = 0

        while True:
            testsize = fsize + 1
            
            lines = []
            exceeded = False
            for word in words:
                if width(word, testsize) > w:
                    exceeded = True

                if not lines:
                    lines.append(word)
                    continue

                if width(lines[-1] + word, testsize) + testsize > w: # +testsize for space
                    lines.append(word)
                else:
                    lines[-1] += ' ' + word

                if height(lines, testsize) > h:
                    exceeded = True

            if exceeded:
                break

            fsize = testsize

        print 'Case #%s: %s' % (tc+1, fsize)

if __name__ == '__main__':
    main()
