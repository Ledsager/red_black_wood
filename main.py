class BinaryTree:
    def __init__(self, data=None, isALeaf=True, colour='r', left=None, right=None):
        self.data = data
        self.isALeaf = isALeaf
        self.colour = colour
        self.left = left
        self.right = right

class BSearchTree:
    def __init__(self, root=None):
        self.root = BinaryTree()

    def insert(self, value):
        self.root = insertVal(self.root, value)
        self.root.colour = 'b'

    def searchPath(self, val):
        path = []
        node = self.root
        while node is not None:
            path.append(node.data)
            if val < node.data:
                node = node.left
            elif val > node.data:
                node = node.right
            else:
                node = None
        return path

def printTree(node, indent=0):
    if node.isALeaf:
        return
    else:
        if node.right is not None:
            printTree(node.right, indent+4)
        print(" "*indent + str(node.data) + node.colour)
        if node.left is not None:
            printTree(node.left, indent+4)


def insertVal(node, value):
        if node.isALeaf:            
            return BinaryTree(value, False, 'r', BinaryTree(None, True, 'b'), BinaryTree(None, True, 'b'))
        elif value > node.data:
            node.right = insertVal(node.right, value)
            if node.colour == 'r':
                return node
            else: 
                if node.right.colour == 'r':
                    if node.right.right.colour == 'r':
                        return rightRightFix(node)
                    elif node.right.left.colour == 'r':
                        return rightLeftFix(node)
                    else:
                        return node
                else:
                    return node
        else: 
            node.left = insertVal(node.left, value)
            if node.colour == 'r':
                return node
            else: 
                if node.left.colour == 'r':
                    if node.left.left.colour == 'r':
                        return leftLeftFix(node)
                    elif node.left.right.colour == 'r':
                        return leftRightFix(node)
                    else:
                        return node
                else:
                    return node

def rightRightFix(node):
    child = node.right
    sib = node.left
    if sib.colour == 'r':
        child.colour = 'b'
        sib.colour = 'b'
        node.colour = 'r'
        return node
    else:
        node.right = child.left
        child.left = node
        child.colour = 'b'
        node.colour = 'r'
        return child

def rightLeftFix(node):
    child = node.right
    sib = node.left
    if sib.colour == 'r':
        child.colour = 'b'
        sib.colour = 'b'
        node.colour = 'r'
        return node
    else:
        grandchild = child.left
        child.left = grandchild.right
        node.right = grandchild.left
        grandchild.left = node
        grandchild.right = child
        grandchild.colour = 'b'
        node.colour = 'r'
        return grandchild

def leftLeftFix(node):
    child = node.left
    sib = node.right
    if sib.colour == 'r':
        child.colour = 'b'
        sib.colour = 'b'
        node.colour = 'r'
        return node
    else:
        node.left = child.right
        child.right = node
        child.colour = 'b'
        node.colour = 'r'
        return child

def leftRightFix(node):
    child = node.left
    sib = node.right
    if sib.colour == 'r':
        child.colour = 'b'
        sib.colour = 'b'
        node.colour = 'r'
        return node
    else:
        grandchild = child.right
        child.right = grandchild.left
        node.left = grandchild.right
        grandchild.right = node
        grandchild.left = child
        grandchild.colour = 'b'
        node.colour = 'r'
        return grandchild


def main():
    myTree = BSearchTree()
    myList = [13,42,88,97,73,80,35,36,88,34,12,92,100,143,1]

    for val in myList:
        myTree.insert(val)

    printTree(myTree.root)
    # print(myTree.searchPath(35))

main()