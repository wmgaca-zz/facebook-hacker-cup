import sys

NORMAL = '.'
EMPTY = 'w'
START = 'x'
DEST = 'o'

class Node(object):

    class Coords(object):
        def __init__(self, coords):
            self.x, self.y = coords

    nodes = None
    start_node = None
    dest_node = None
    tree_width = None
    tree_height = None

    def __init__(self, value, coords):
        self.value = value
        self.coords = Node.Coords(coords)
        self.visited = False

        self.f = None
        self.h = None
        if value == START: self.f = 0

        if self.value == START: Node.start_node = self
        elif self.value == DEST: Node.dest_node = self

    @property
    def g(self):
        if self.f is None: self.update_f()
        
        g = self.f

        if self.h: g += self.h
        else: g += self.approximate_h()

        return g

    def update_f(self):
        for neighbour in self.get_neighbours():
            if neighbour.f is not None:
                if not self.f:
                    self.f = neighbour.f + 1
                elif neighbour.f + 1 < self.f:
                    self.f = neighbour.f + 1
                    return True
        return False

    @property
    def x(self):
        if not self.coords: return None
        return self.coords.x

    @property
    def y(self):
        if not self.coords: return None
        return self.coords.y

    def __repr__(self):
        return 'Node(%d, %d: %s (%s)' % (self.x, self.y, self.value, self.f)

    def get_neighbours(self):
        # left, right, top, bottom
        coords = [Node.Coords((self.x - 1, self.y)), 
                  Node.Coords((self.x + 1, self.y)), 
                  Node.Coords((self.x, self.y - 1)),
                  Node.Coords((self.x, self.y + 1))]

        neighbours = []

        for c in coords:
            if 0 <= c.x < Node.tree_width and 0 <= c.y < Node.tree_height:
                if Node.nodes[c.y][c.x].value != EMPTY:
                    neighbours.append(Node.nodes[c.y][c.x])
            
        return neighbours

    def approximate_h(self):
        return abs(Node.dest_node.x - self.x) + abs(    Node.dest_node.y - self.y)

    @staticmethod
    def print_nodes(coords=None, opened=None):
        #string = chr(201) + (Node.tree_width) * chr(205) + chr(187) + '\n'
        string = '+' + (Node.tree_width) * '-' + '+\n'

        for line in Node.nodes:
            string += '|'  #chr(186)

            for node in line:
                if coords and node.x == coords.x and node.y == coords.y:
                    string += 'x'  #chr(219)
                elif node.visited:
                    string += ' '
                elif opened and node in opened:
                    g = node.g
                    if g > 9:
                        g -= 10;
                    string += '%s' % g
                else:
                    string += node.value
                """
                elif node.value == EMPTY:
                    string += EMPTY #chr(178)
                elif node.value == NORMAL:
                    string += chr(176)
                elif node.value == START:
                    string += 'X'
                elif node.value == DEST:
                    string += 'O'
                """
            string += '|\n'  #chr(186) + '\n'

        #string += chr(200) + (Node.tree_width) * chr(205) + chr(188)
        string += '+' + (Node.tree_width) * '-' + '+\n'

        print string

def find_path(file_path):
    input_file = open(file_path)
    data = [[char for char in line] for line in input_file.read().split('\n') if line]
 
    Node.tree_width = len(data[0])
    Node.tree_height = len(data)
    
    Node.nodes = [[] for y in xrange(Node.tree_height)]
    for y in xrange(Node.tree_height):
        for x in xrange(Node.tree_width):
            Node.nodes[y].append(Node(data[y][x], (x, y)))

    if not Node.start_node or not Node.dest_node:
        print 'Not gonna happen...'
        return
  
    opened, visited, current = [], [], Node.start_node
    
    counter = 0

    print ''
    Node.print_nodes(current.coords, opened)
    
    raw_input()

    while True:
        # check if destination
        if current.value == DEST:
            Node.print_nodes()
            return current.f

        # mark current as visited
        current.visited = True
        visited.append(current)

        # add neighbours to opened
        for node in current.get_neighbours():
            if node not in visited and node not in opened:
                node.update_f()
                opened.append(node)

        Node.print_nodes(current.coords, opened)

        # TODO(wmgacax): improve this (check if destination is a neighbour, etc.)
        # TODO(wmgacax): let's keep this in a dict...
        #     {g: [node, node, node], g2: [node]}
        #   or list:
        #     [[g, [node, node]], [g2, [node, node]]]


        # get most promising node for the next step
        if not opened: return None
        best = 0
        print "best g: %s" % opened[best].g
        for i in xrange(len(opened)):
            if opened[i].g < opened[best].g:
                print "-> %s" % opened[i].g
                best = i
            elif opened[i].g == opened[best].g and opened[i].f < opened[best].f:
                best = i
        current = opened[best]
        opened.pop(best)         
        
        raw_input()

if __name__ == '__main__':
    if len(sys.argv) == 2:
        result = find_path(sys.argv[1])
        if result:
            print 'Found path, steps: %d' % result
        else:
            print 'Over my dead body'
    else:
        print 'Input?'
