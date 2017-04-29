#!/usr/bin/env python
import heapq

"""
Huffman Coding Algorithm

Pseudocode:
Q = priority queue of all symbols
While length(Q) > 0:
    If length(Q) = 1:
        N = final node
        return N
    N1,N2 = nodes for two lowest probability symbols
    IN1 = new internal (empty) node
    N1.parent, N2.parent = IN1
    IN1.probabality = N1.probability + N2.probability
    Q.insert(IN1)



"""

class huffman_node(object):
    def __init__(self, left_child=None, right_child=None, parent=None, symbol=None):
        self.left_child = left_child
        self.right_child = right_child
        self.parent = parent
        self.symbol = symbol

    def has_children(self):
        if self.left_child == None and self.right_child == None:
            return False
        return True

    def __repr__(self):
        return str(self.symbol)


def huffman(codeDict):
    Q = []
    for code in codeDict:
        node = huffman_node(symbol=code[1])
        heapq.heappush(Q,(code[0],node))
    while len(Q) > 1:
        n1 = heapq.heappop(Q)
        n2 = heapq.heappop(Q)
        inner_node = huffman_node(n2[1], n1[1])
        n1[1].parent = inner_node
        n2[1].parent = inner_node
        heapq.heappush(Q, (n1[0]+n2[0], inner_node))
    return heapq.heappop(Q)

def load_symbols(filename):
    """ Generate symbol list from text file """
    file = open(filename, 'r')
    # Map each line of test data to a line in the data list:
    data = [ (int(x.strip()), i) for i, x in enumerate(file)]
    return data


if __name__ == '__main__':
    codes = [(0.32,'A')
            ,(0.25,'B')
            ,(0.2,'C')
            ,(0.18,'D')
            ,(0.05,'E')
            ]
    codes = load_symbols("data_huffman.txt")
    root = huffman(codes)[1]
    codeList = []
    def walk_tree(node, codeList, prefix="", code={}):
        if node.has_children() == False:
            codeList.append((prefix, node.symbol))
        if isinstance(node.left_child, huffman_node):
            walk_tree(node.left_child, codeList, prefix+"0", code)
        if isinstance(node.right_child, huffman_node):
            walk_tree(node.right_child, codeList, prefix+"1", code)

    walk_tree(root, codeList)
    print(min([ len(x[0]) for x in codeList]))
