################################################################################
# Name: Blake Perrin
# Date: 03/15/23
# Description: This program is designed to create a linked list with a size
#              specified by the user. The program outputs the original list
#              along with the head and tail data, and then sorts the data using
#              the selection sort. The new head and tail data is then outputed
#              to the user.
################################################################################

# import the random module to generate random data for the nodes
from random import randint

# A node class defining a Node. The class includes the ability to set
# the data and the link for each node.
# I used inspiration from an earlier course to help me with this.
class Node:
    # Constructor.
    def __init__(self, data):
        self.data = data
        self.link = None

    # Accessor for data.
    @property
    def data(self):
        return self._data
    
    # Setter for data.
    @data.setter
    def data(self, value):
        self._data = value

    # Accessor for link.
    @property
    def link(self):
        return self._link

    # Setter for link.
    @link.setter
    def link(self, value):
        self._link = value

    # Defines how a node should be printed.
    def __str__(self):
        return str(self.data)
    
class LinkedList:
    # Constructor.
    def __init__(self, num_nodes, head):
        self.num_nodes = num_nodes
        self.head = head
        self.tail = None

    # Accessor for num_nodes.
    @property
    def num_nodes(self):
        return self._num_nodes
    
    # Setter for num_nodes.
    @num_nodes.setter
    def num_nodes(self, num_nodes):
        self._num_nodes = num_nodes

    # Accessor for head.
    @property
    def head(self):
        return self._head

    # Setter for head.
    @head.setter
    def head(self, head):
        self._head = head

    # Accessor for tail.
    @property
    def tail(self):
        return self._tail

    # Setter for tail.
    @tail.setter
    def tail(self, tail):
        self._tail = tail

    # A function to append a new node to the linked list.
    def append(self, node):
        p = self.head
        while(p.link != None):
            p = p.link
        p.link = node
        self.tail = node

    # A function to sort a linked list. The function requires the head
    # node of the list to be provided as well as the length of the list.
    # I used: https://www.geeksforgeeks.org/python-program-for-selection-sort/ 
    # to help me with the basics of the algorithm.
    def selection_sort(self):
        start = self.head
        for i in range(self.num_nodes):
            p = start
            curr = start
            while p.link != None:
                next = p.link
                if next.data < curr.data:
                    curr = next
                p = p.link
            temp = start.data
            start.data = curr.data
            curr.data = temp
            start = start.link

    # A Function to print all nodes in the linked list.
    def printList(self):
        p = self.head
        while(p != None):
            print(p.data, "", end="")
            p = p.link
        print()


################################################################################
# Other Functions
################################################################################

# A function to convert words into an integer.
# I took this code from: https://stackoverflow.com/questions/493174/is-there-a-way-to-convert-number-words-to-integers
# The code takes in written numbers and converts them to integers.
# It also detects if an invalid word is used and exits the program properly.
def text2int(textnum, numwords={}):
    if not numwords:
      units = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen",
      ]

      tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

      scales = ["hundred", "thousand", "million", "billion", "trillion"]

      numwords["and"] = (1, 0)
      for idx, word in enumerate(units):    numwords[word] = (1, idx)
      for idx, word in enumerate(tens):     numwords[word] = (1, idx * 10)
      for idx, word in enumerate(scales):   numwords[word] = (10 ** (idx * 3 or 2), 0)

    current = result = 0
    for word in textnum.split():
        if word not in numwords:
          print("Invalid word: " + word)
          exit(0)

        scale, increment = numwords[word]
        current = current * scale + increment
        if scale > 100:
            result += current
            current = 0

    return result + current

################################################################################
# Main Function
################################################################################

# Main Program
if __name__ == "__main__":

    # Ask the user for the number of nodes.
    num_nodes = input("Please, enter the number of nodes: ").lower()

    # Check if the input is an integer.
    try:
        num_nodes = int(num_nodes)

        # If it is an integer but equals 0.
        if num_nodes == 0:
            exit(0)

        # If it is an integer and negative, convert it to a positive integer.
        elif num_nodes < 0:
            num_nodes = num_nodes*(-1)

    # If it is not an integer, convert the text to an integer.
    except ValueError:
        num_nodes = int(text2int(num_nodes))

    # Initiate the linked list as well as the head node.
    n = Node(randint(0,100))
    List1 = LinkedList(num_nodes, n)

    # Populate the list using the number of nodes provided by the user.
    for i in range(num_nodes - 1):
        n = Node(randint(0,100))
        List1.append(n)

    # Print the unsorted list as well as head and tail data.
    print("Unsorted List: ", end="")
    List1.printList()
    print("Head Data: {}".format(List1.head))
    print("Tail Data: {}".format(List1.tail))
    print()

    # Sort the list and print the sorted list as well as head and tail data.
    List1.selection_sort()
    print("Sorted List: ", end="")
    List1.printList()
    print("Head Data: {}".format(List1.head))
    print("Tail Data: {}".format(List1.tail))