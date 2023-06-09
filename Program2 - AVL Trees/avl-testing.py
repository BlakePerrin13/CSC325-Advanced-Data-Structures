import sys

class AVLTree:
    def __init__(self, root = None):
        self.root = root

    class AVLNode:
        def __init__(self, item, balance = 0, left = None, right = None):
            self.item = item
            self.left = left
            self.right = right
            self.balance = balance

        def getBalance(self):
            return self.balance
        
        def setBalance(self, balance):
            self.balance = balance

        def __repr__(self):
            return f"AVLNode({repr(self.item)}, balance = {repr(self.balance)}, left = {repr(self.left)}, right = {repr(self.right)})"

        def __iter__(self):
            if self.left != None:
                for elem in self.left:
                    yield elem

            yield self.item

            if self.right != None:
                for elem in self.right:
                    yield elem
                    
        def _getLeaves(self):
            # trivial case
            # empty tree
            if self == None:
                return
            
            # if no children -> print item
            if self.left == None and self.right == None:
                print(self.item, end=" ")
            
            # if left child -> go left
            if self.left != None:
                self.left._getLeaves()

            # if right child -> go right
            if self.right != None:
                self.right._getLeaves()
            
                       
    def insert(self, item):

        def rotateRight(pivot):
            # pivot becomes right child of bad child
            # bad child's right child becomes pivot's left child

            # get pivot's left child node (bad child)
            leftChild = pivot.left

            ### WRITE YOUR CODE HERE ###

            pivot.left = leftChild.right
            leftChild.right = pivot
                
            # return bad child
            return leftChild
        
        def rotateLeft(pivot):
            # pivot becomes left child of bad child
            # bad child's left child becomes pivot's right child
            
            # get pivot's right child node (bad child)
            rightChild = pivot.right

            ### WRITE YOUR CODE HERE ###
            pivot.right = rightChild.left
            rightChild.left = pivot
            
            # return bad child
            return rightChild

        def __insert(root, item):
            # if empty tree, create a node with given item
            if root == None:
                return AVLTree.AVLNode(item)

            # item to be inserted is smaller than root
            # inserting into left subtree with specific rules to handle
            if item < root.item:
                root.left = __insert(root.left, item)

                # handle Case 1 & Case 2 with no rotations
                ### WRITE YOUR CODE HERE ###

                # Case 1
                if root.getBalance() == 0:
                    print("CASE 1:")
                    if self.pivotFound == False:
                        if root.right == None:
                            root.setBalance(root.getBalance() - 1)
                            # print("Node: {}, Balance: {}".format(root.item, root.getBalance()))
                        else:
                            rightHeight = root.right.getBalance()
                            if rightHeight < 0:
                                rightHeight *= -1
                            leftHeight = root.left.getBalance()
                            if leftHeight < 0:
                                leftHeight *= -1
                            root.setBalance(rightHeight - leftHeight)
                    print(root)
                    print()
                elif root.getBalance() != 0:
                    print("CASE 2:")
                    if self.pivotFound == False:
                        print("Pivot Now found: {}".format(root))
                        self.pivotFound = True
                        root.setBalance(root.getBalance() - 1)
                    print(root)
                    print()

                # check for Case 3 when AVL is unbalanced
                if root.getBalance() == -2:
                    # bad child must be left child, since we are in the left subtree
                    badChild = root.left

                    # Subcase A - Single Rotation
                    # must be a right rotation
                    ### WRITE YOUR CODE HERE ###
                    if item < badChild.item:
                        print("Rotate Right")
                        print("Root Node: {}".format(root))
                        print("Bad Child: {}".format(badChild))

                        root = rotateRight(root)
                        root.left.setBalance(0)
                        if root.right.left == None:
                            root.right.setBalance(0)
                        else:
                            root.right.setBalance(-1)
                        self.pivotFound = True
                        root.setBalance(root.getBalance() + 1)
                        print(root)
                        print()

                    # Subcase B - Double Rotation
                    # rotate at bad child, and rotate at pivot based on where bad grandchild is

                    ### WRITE YOUR CODE HERE ###
                    if item > badChild.item:
                        pivot = root
                        tempBadChild = badChild
                        badGrandChild = badChild.right

                        print("Pivot: {}".format(root))
                        print("Bad Child: {}".format(badChild))
                        print("Bad Grandchild: {}".format(badGrandChild))
                        print()

                        badChild = rotateLeft(badChild)

                        root.left = badChild

                        print("After First Rotation:")
                        print("Pivot: {}".format(root))
                        print("Bad Child: {}".format(badChild))
                        print("Bad Grandchild: {}".format(badGrandChild))
                        print()

                        root = rotateRight(root)

                        print("After Second Rotation:")
                        print("Root: {}".format(root))
                        print("Bad Child: {}".format(badChild))
                        print("TempBC: {}".format(tempBadChild))
                        print("Bad Grandchild: {}".format(badGrandChild))
                        print("Pivot: {}".format(pivot))
                        print()

                        # adjusting balances of pivot and bad child based on bad grandchild
                        # if value inserted at badGrandChild
                        # then pivot balance = 0, bad child balance = 0
                        ### WRITE YOUR CODE HERE ###
                        if item == badGrandChild.item:
                            pivot.setBalance(0)
                            tempBadChild.setBalance(0)

                        # if inserted value smaller than bad grandchild (left subtree)
                        # then pivot balance = 1, bad child balance = 0
                        ### WRITE YOUR CODE HERE ###
                        if item < badGrandChild.item:
                            pivot.setBalance(1)
                            tempBadChild.setBalance(0)
                        
                        # if inserted value larger than bad grandchild (right subtree)
                        # then pivot balance = 0, bad child = -1
                        ### WRITE YOUR CODE HERE ###
                        if item > badGrandChild.item:
                            pivot.setBalance(0)
                            tempBadChild.setBalance(-1)

                        self.pivotFound = True
                        root.setBalance(root.getBalance() - 1)

            # item to be inserted is larger than root
            # inserting into right subtree with specific rules to handle
            elif item > root.item:

                root.right = __insert(root.right, item)

                # handle Case 1 & Case 2 with no rotations
                ### WRITE YOUR CODE HERE ###
                if root.getBalance() == 0:
                    print("CASE 1:")
                    if self.pivotFound == False:
                        if root.left == None:
                            root.setBalance(root.getBalance() + 1)
                            # print("Node: {}, Balance: {}".format(root.item, root.getBalance()))
                        else:
                            rightHeight = root.right.getBalance()
                            if rightHeight < 0:
                                rightHeight *= -1
                            leftHeight = root.left.getBalance()
                            if leftHeight < 0:
                                leftHeight *= -1
                            root.setBalance(rightHeight - leftHeight)
                    print(root)
                    print()
                elif root.getBalance() != 0:
                    print("CASE 2:")
                    if self.pivotFound == False:
                        print("Pivot Now found: {}".format(root))
                        self.pivotFound = True
                        root.setBalance(root.getBalance() + 1)
                    print(root)
                    print()
                    
                # check for Case 3 when AVL is unbalanced
                if root.getBalance() == 2:
                    # bad child must be right child, since we are in the right subtree
                    badChild = root.right

                    # Subcase A - Single Rotation
                    ### WRITE YOUR CODE HERE ###
                    if item > badChild.item:
                        print("Rotate Left")
                        print("Root Node: {}".format(root))
                        print("Bad Child: {}".format(badChild))

                        root = rotateLeft(root)
                        root.right.setBalance(0)
                        if root.left.right == None:
                            root.left.setBalance(0)
                        else:
                            root.left.setBalance(-1)
                        self.pivotFound = True
                        root.setBalance(root.getBalance() - 1)
                        print(root)
                        print()

                    # Subcase B - Double Rotation
                    ### WRITE YOUR CODE HERE ###
                    if item < badChild.item:
                        pivot = root
                        tempBadChild = badChild
                        badGrandChild = badChild.left

                        print("Pivot: {}".format(root))
                        print("Bad Child: {}".format(badChild))
                        print("Bad Grandchild: {}".format(badGrandChild))
                        print()

                        badChild = rotateRight(badChild)

                        root.right = badChild

                        print("After First Rotation:")
                        print("Pivot: {}".format(root))
                        print("Bad Child: {}".format(badChild))
                        print("Bad Grandchild: {}".format(badGrandChild))
                        print()

                        root = rotateLeft(root)

                        print("After Second Rotation:")
                        print("Root: {}".format(root))
                        print("Bad Child: {}".format(badChild))
                        print("TempBC: {}".format(tempBadChild))
                        print("Bad Grandchild: {}".format(badGrandChild))
                        print("Pivot: {}".format(pivot))
                        print()

                        # adjusting balances of pivot and bad child based on bad grandchild
                        # if value inserted at badGrandChild
                        # then pivot balance = 0, bad child balance = 0
                        ### WRITE YOUR CODE HERE ###
                        if item == badGrandChild.item:
                            pivot.setBalance(0)
                            tempBadChild.setBalance(0)
                            
                        
                        # if inserted value smaller than bad grandchild (left subtree)
                        # then pivot balance = 0, bad child balance = 1
                        ### WRITE YOUR CODE HERE ###
                        elif item < badGrandChild.item:
                            pivot.setBalance(0)
                            tempBadChild.setBalance(1)
                        
                        # if inserted value larger than bad grandchild (right subtree)
                        # then pivot balance = -1, bad child = 0
                        ### WRITE YOUR CODE HERE ###
                        else:
                            pivot.setBalance(-1)
                            tempBadChild.setBalance(0)

                        self.pivotFound = True
                        root.setBalance(root.getBalance() + 1)
            
                        
            # check if inserting duplicated value
            else:
                print(f"Inserting duplicated value... {item}")
                raise Exception("Duplicate value")

            # once done __inserting return root
            # print(root)
            return root
        
        # once done inserting update pivotFound value
        # and assign root with __insert return
        self.pivotFound = False
        self.root = __insert(self.root, item)

    # repr on tree calls repr on root node
    def __repr__(self):
        return f"AVLTree: {repr(self.root)}"

    # iter on tree calls iter on root node
    def __iter__(self):
        return iter(self.root)

    def __lookup(node, item):
        # returns True if value is in tree and False otherwise
        if node == None:
            return False
        
        ### WRITE YOUR CODE HERE ###
        # if reached node with lookup item -> return True
        if node.item == item:
            return True

        # if item is larger than node item -> go right
        if item > node.item:
            return AVLTree.__lookup(node.right, item)

        # if item is smaller than node item -> go left
        if item < node.item:
            return AVLTree.__lookup(node.left, item)

    def __contains__(self, item):
        # checks if item is in the tree
        # runs __lookup on the tree root
        return AVLTree.__lookup(self.root, item)

    def leaves(self):
        # finds tree leaves
        self.root._getLeaves()  

def main():
    tree = AVLTree()

    # get values from input file
    file = open(sys.argv[1], "r")
    for line in file:
        values = line.split()

    print(f"Values to be inserted: {values}")
    print()
    
    # insert values into the AVL tree
    for v in values:
        tree.insert(int(v))
        print(f"Value {v} is inserted.")
    print()

    # print out the tree
    print(repr(tree))
    print()
    
    # print out tree in-order traversal
    print("In-order traversal: ", end = "")
    for node in tree:
        print(node, end = " ")    
    print()

    # print out tree leaves
    print("\nLeaves: ", end = "")
    tree.leaves()
    print()
    
    # check if given values are in the tree
    print()
    for val in [10, 17, 35, 38, 40]:
        if (val in tree):
            print(f"Value {val} is in tree")
        else:
            print(f"Value {val} is not in tree")  

main()
