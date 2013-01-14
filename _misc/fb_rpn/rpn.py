import sys

def enum(**kwargs):
    return type('Enum', (), kwargs)

def Node(object):

    _options = enum(default=1, remove=2, add_x=3, add_o=4, replace=5)
    _

    def __init__(self, expression, parent=None, option=None):
        if not parent:
            self.left = []
            self.right = expression
        else:
            self.left = parent.left
            self.right = parent.right
            
            if option == self._options.remove:
                self.right.pop(0)
            elif option == self._options.add_x:
                self.right.insert(0, 'x')
            elif option == self._options.add_o:
                self.right.insert(0, '*')
            elif option == self._option.replace:
                if self.right[0] == 'x':
                    self.right[0] = '*'
                else:
                    self.right[0] = 'x'

            self.execute_step()
            
    def _check_options(self):
        options = []

        if not len(self.right):
            return

    def execute_step(self):
        if not self.right:
            return False
        if self.right[0] == 'x':
            self.left.append(self.right.pop(0))
        else:
            self.left.pop()
            self.right.pop(0)
        return True

def rpn(expression):
    root = Node([x for x in expression])

if __name__ == '__main__':
    try:
        rpn(sys.argv[1])
    except KeyError:
        print('Expression?')
