from python_util.ds import tree

def build_tree(filename):
    """Builds and returns a tree.
    """
    with open(filename, 'r') as in_file:
        root = None
        parent = None
        grandparent = None
        for line in in_file:
            if root is None:
                root = tree.Tree(int(line))
                parent = root
            else:
                grandparent_offset = 0
                for i, attr in enumerate(line.split(' ')):
                    if i > 0 and not i % 2:
                        grandparent_offset += 1
                        parent = grandparent[grandparent_offset / 2]
                    parent.append(tree.Tree(int(attr)))
                grandparent = grandparent[0] if grandparent is not None \
                              else parent
                parent = grandparent[0]

    return root

def max_sum(root):
    """Builds max sum using DP.

    Args:
        root - List representation of a tree
    """
    print '%s %s' % (root[-1], len(root[-1]))
    if len(root) == 1:
        return root[0][0]
    row = root[-1]
    root = root[:-1]
    max_every = [max(row[i], row[i+1]) for i in xrange(len(row) - 1)]
    root[-1] = [a + b for a, b in zip(max_every, root[-1])]
    return max_sum(root)

def main():
    t = build_tree('problem-18/triangle.txt')
    print max_sum(tree.Tree.list_repr(t))

if __name__ == '__main__':
    main()