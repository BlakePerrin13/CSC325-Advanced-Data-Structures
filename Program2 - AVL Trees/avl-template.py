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
            
            # if no children -> print item.
            if self.left == None and self.right == None:
                print(self.item, end=" ")
            
            # if left child -> go left.
            if self.left != None:
                self.left._getLeaves()

            # if right child -> go right.
            if self.right != None:
                self.right._getLeaves()
            
                       
    def insert(self, item):

        # Function to rotate a subtree to the right.
        def rotateRight(pivot):
            # pivot becomes right child of bad child.
            # bad child's right child becomes pivot's left child.

            # get pivot's left child node (bad child).
            leftChild = pivot.left

            ### WRITE YOUR CODE HERE ###

            # if the left child (Bad Child) has a right node, this node will be moved to be left child of the pivot,
            # which will eventually become the right child of the bad child. If the left child (Bad Child) does not
            # have a right node, the left child of the pivot will be assigned "None".
            pivot.left = leftChild.right

            # change the right child of the bad child to the pivot, this is ultimately the right rotation.
            leftChild.right = pivot
                
            # return bad child, this sets the leftChild to be the new root or pivot node.
            return leftChild
        
        def rotateLeft(pivot):
            # pivot becomes left child of bad child.
            # bad child's left child becomes pivot's right child.
            
            # get pivot's right child node (bad child).
            rightChild = pivot.right

            ### WRITE YOUR CODE HERE ###

            # if the right child (Bad Child) has a left node, this node will be moved to be right child of the pivot,
            # which will eventually become the left child of the bad child. If the right child (Bad Child) does not
            # have a left node, the right child of the pivot will be assigned "None".
            pivot.right = rightChild.left

            # change the left child of the bad child to the pivot, this is ultimately the left rotation.
            rightChild.left = pivot
            
            # return bad child, this sets the rightChild to be the new root or pivot node.
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

                # Case 1, the balance of the current node is equal to 0.
                if root.getBalance() == 0:

                    # Check if a pivot has been found. If no pivot has been found, continue setting the balance.
                    # Otherwise, skip this node.
                    if self.pivotFound == False:

                        # Since we are in the left subtree, if there is no right child, subtract one from the node's current balance.
                        if root.right == None:
                            root.setBalance(root.getBalance() - 1)
                        
                        # Otherwise take the absolute value of the right child (height of the right subtree) and subtract the
                        # absolute value of the left Child (height of the left subtree) from it.
                        else:
                            rightHeight = root.right.getBalance()
                            # Very ugly way to get the absolute value ...
                            if rightHeight < 0:
                                rightHeight *= -1

                            leftHeight = root.left.getBalance()
                            # Very ugly way to get the absolute value ...
                            if leftHeight < 0:
                                leftHeight *= -1
                            
                            # Subtract the height of the right subtree from the left and set the current node's balance to that value.
                            root.setBalance(rightHeight - leftHeight)

                # Case 2, the balance of the current node is not equal to 0.
                elif root.getBalance() != 0:

                    # Check if a pivot has been found. If no pivot has been found, continue setting the balance.
                    # Otherwise, skip this node.
                    if self.pivotFound == False:
                        
                        # Since this node does not have a balance of 0 and a pivot has not been found, this node is now the pivot.
                        self.pivotFound = True

                        # Since we are in the left subtree, subtract one from the balance.
                        root.setBalance(root.getBalance() - 1)

                # check for Case 3 when AVL is unbalanced
                # Case 3, the balance of the current node is equal to -2.
                if root.getBalance() == -2:

                    # bad child must be left child, since we are in the left subtree
                    badChild = root.left

                    # Subcase A - Single Rotation
                    # Since we are in the left subtree, Subcase A defines a node being inserted in the direction of the unbalance.

                    ### WRITE YOUR CODE HERE ###

                    # Defines the condition for Subcase A in the left subtree (item < badChild's item).
                    if item < badChild.item:

                        # Set the root node to the output node returned by the rotateRight function.
                        # Since we are in the left subtree and in Subcase A we are rotating right.
                        root = rotateRight(root)

                        # Set the balance of the left node of the root to 0.
                        root.left.setBalance(0)

                        # if the right child of the root does not have a left child, set the balance of the right child of the root to 0.
                        if root.right.left == None:
                            root.right.setBalance(0)

                        # Otherwise, set the balance of the right child of the root to -1 (Right Rotation may move a value to the left
                        # child of the right child of the root node).
                        else:
                            root.right.setBalance(-1)

                        # We have found a pivot node, set pivotFound to True.
                        self.pivotFound = True

                        # We have balanced the root/pivot by rotating right. Update the balance by increasing it by 1.
                        root.setBalance(root.getBalance() + 1)

                    # Subcase B - Double Rotation
                    # rotate at bad child, and rotate at pivot based on where bad grandchild is
                    # Since we are in the left subtree, Subcase B defines a node being inserted in the direction opposite of the unbalance.

                    ### WRITE YOUR CODE HERE ###

                    # Defines the condition for Subcase B in the left subtree (item > badChild's item).
                    if item > badChild.item:

                        # Temporary Placeholders for pivot and bad child.
                        pivot = root
                        tempBadChild = badChild

                        # Since we are in the left subtree and inserting to the right, the bad grandchild is the 
                        # right child of the bad child.
                        badGrandChild = badChild.right

                        # Set the badChild node to the output node returned by the rotateLeft function.
                        # Since we are in the left subtree and in Subcase B we are rotating left first.
                        badChild = rotateLeft(badChild)

                        # Set the left child of the root/pivot node to be the badChild. This updates the tree to accept the first rotation.
                        root.left = badChild

                        # Set the root node to the output node returned by the rotateRight function.
                        # Since we are in the left subtree and in Subcase B, and since we already completed the first rotation, 
                        # we are now rotating to the right.
                        root = rotateRight(root)

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

                        # We have found a pivot node, set pivotFound to True.
                        self.pivotFound = True

                        # We have balanced the root/pivot by rotating left and then rotating right. Update the balance by decreasing it by 1.
                        root.setBalance(root.getBalance() - 1)


            # item to be inserted is larger than root
            # inserting into right subtree with specific rules to handle
            elif item > root.item:

                root.right = __insert(root.right, item)

                # handle Case 1 & Case 2 with no rotations
                ### WRITE YOUR CODE HERE ###

                # Case 1, the balance of the current node is equal to 0.
                if root.getBalance() == 0:

                    # Check if a pivot has been found. If no pivot has been found, continue setting the balance.
                    # Otherwise, skip this node.
                    if self.pivotFound == False:

                        # Since we are in the right subtree, if there is no left child, add one to the node's current balance.
                        if root.left == None:
                            root.setBalance(root.getBalance() + 1)
                        
                        # Otherwise take the absolute value of the right child (height of the right subtree) and subtract the
                        # absolute value of the left Child (height of the left subtree) from it.
                        else:
                            rightHeight = root.right.getBalance()
                            # Very ugly way to get the absolute value ...
                            if rightHeight < 0:
                                rightHeight *= -1

                            leftHeight = root.left.getBalance()
                            # Very ugly way to get the absolute value ...
                            if leftHeight < 0:
                                leftHeight *= -1

                            # Subtract the height of the right subtree from the left and set the current node's balance to that value.
                            root.setBalance(rightHeight - leftHeight)

                # Case 2, the balance of the current node is not equal to 0.
                elif root.getBalance() != 0:

                    # Check if a pivot has been found. If no pivot has been found, continue setting the balance.
                    # Otherwise, skip this node.
                    if self.pivotFound == False:

                        # Since this node does not have a balance of 0 and a pivot has not been found, this node is now the pivot.
                        self.pivotFound = True

                        # Since we are in the right subtree, add one to the balance.
                        root.setBalance(root.getBalance() + 1)
                    
                # check for Case 3 when AVL is unbalanced
                # Case 3, the balance of the current node is equal to 2.
                if root.getBalance() == 2:

                    # bad child must be right child, since we are in the right subtree
                    badChild = root.right

                    # Subcase A - Single Rotation
                    # Since we are in the right subtree, Subcase A defines a node being inserted in the direction of the unbalance.

                    ### WRITE YOUR CODE HERE ###

                    # Defines the condition for Subcase A in the right subtree (item > badChild's item).
                    if item > badChild.item:

                        # Set the root node to the output node returned by the rotateLeft function.
                        # Since we are in the right subtree and in Subcase A we are rotating left.
                        root = rotateLeft(root)

                        # Set the balance of the right node of the root to 0.
                        root.right.setBalance(0)

                        # if the left child of the root does not have a right child, set the balance of the left child of the root to 0.
                        if root.left.right == None:
                            root.left.setBalance(0)

                        # Otherwise, set the balance of the left child of the root to 1 (Left Rotation may move a value to the right
                        # child of the left child of the root node).
                        else:
                            root.left.setBalance(1)

                        # We have found a pivot node, set pivotFound to True.
                        self.pivotFound = True

                        # We have balanced the root/pivot by rotating left. Update the balance by decreasing it by 1.
                        root.setBalance(root.getBalance() - 1)

                    # Subcase B - Double Rotation
                    # rotate at bad child, and rotate at pivot based on where bad grandchild is
                    # Since we are in the right subtree, Subcase B defines a node being inserted in the direction opposite of the unbalance.

                    ### WRITE YOUR CODE HERE ###

                    # Defines the condition for Subcase B in the right subtree (item < badChild's item).
                    if item < badChild.item:

                        # Temporary Placeholders for pivot and bad child.
                        pivot = root
                        tempBadChild = badChild

                        # Since we are in the right subtree and inserting to the left, the bad grandchild is the 
                        # left child of the bad child.
                        badGrandChild = badChild.left

                        # Set the badChild node to the output node returned by the rotateRight function.
                        # Since we are in the right subtree and in Subcase B we are rotating right first.
                        badChild = rotateRight(badChild)

                        # Set the right child of the root/pivot node to be the badChild. This updates the tree to accept the first rotation.
                        root.right = badChild

                        # Set the root node to the output node returned by the rotateLeft function.
                        # Since we are in the right subtree and in Subcase B, and since we already completed the first rotation, 
                        # we are now rotating to the left.
                        root = rotateLeft(root)

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

                        # We have found a pivot node, set pivotFound to True.
                        self.pivotFound = True

                        # We have balanced the root/pivot by rotating right and then rotating left. Update the balance by increasing it by 1.
                        root.setBalance(root.getBalance() + 1)
            
                        
            # check if inserting duplicated value.
            else:
                print(f"Inserting duplicated value... {item}")
                raise Exception("Duplicate value")

            # once done __inserting return root
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
        # returns True if value is in tree and False otherwise.
        if node == None:
            return False
        
        ### WRITE YOUR CODE HERE ###

        # if reached node with lookup item -> return True.
        if node.item == item:
            return True

        # if item is larger than node item -> go right.
        if item > node.item:
            return AVLTree.__lookup(node.right, item)

        # if item is smaller than node item -> go left.
        if item < node.item:
            return AVLTree.__lookup(node.left, item)

    def __contains__(self, item):
        # checks if item is in the tree.
        # runs __lookup on the tree root.
        return AVLTree.__lookup(self.root, item)

    def leaves(self):
        # finds tree leaves.
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
