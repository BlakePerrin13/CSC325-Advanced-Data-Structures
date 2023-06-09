import sys

DEBUG = False

class Heap:
    def __init__(self):
        self.size = 0
        self.capacity = 1
        self.data = [None]
        
    def getData(self):
        return self.data[:self.size]
    def getSize(self):
        return self.size
    def isEmpty(self):
        return self.size == 0

    def __siftUp(self, child):
        parent = (child - 1) // 2
        while (child > 0) and (self.data[child] > self.data[parent]):
            temp = self.data[child]
            self.data[child] = self.data[parent]
            self.data[parent] = temp
            if DEBUG:
                print(f"{self.data[parent]} swapped with {self.data[child]}")
            child = parent
            parent = (child - 1) // 2

    def buildFrom(self, seq):
        self.data = [None]*len(seq)
        self.size = self.capacity = len(seq)

        for x in range(self.size):
            self.data[x] = seq[x]
            
        index = (2 * self.data.index(seq[0])) + 1

        while (index < len(seq)):
            self.__siftUp(index)
            index += 1

    def addToHeap(self, newVal):
        if (self.size == self.capacity):
            self.capacity *= 2
            temp = [None] * self.capacity
            
            for i in range(self.size):
                temp[i] = self.data[i]
                
            self.data = temp

        self.data[self.size] = newVal
        self.__siftUp(self.size)
        self.size += 1
        
        return newVal

    def __largestChild(self, index, lastIndex):
        ''' Inputs:
            - index -> index of the current node
            - lastIndex -> index of the last node in the heap
            Output:
            - index of the largest child if it exists, None otherwise
        '''

        # find indexes of left and right child of the current (index) node
        # return None if left child index is past last index
        # otherwise return the index of the largest child

        ### WRITE YOUR CODE HERE ###

        # Get the left and right child indexes
        leftChildIndex = (2 * index) + 1
        rightChildIndex = (2 * index) + 2

        # Check if the left child index is past the last index
        if leftChildIndex > lastIndex:
            return None
        
        # Check if the right child index is past the last index
        elif rightChildIndex > lastIndex:
            return leftChildIndex
        
        # Otherwise check which child is larger
        else:
            # If the left child is larger, return the left child index
            if self.data[leftChildIndex] > self.data[rightChildIndex]:
                return leftChildIndex
            
            # Otherwise if the right child is larger, return the right child index
            else:
                return rightChildIndex

    def __siftDownFromTo(self, fromIndex, last):
        ''' Inputs:
            - fromIndex -> index of the node where to start sifting from
            - last -> index of the last node in the heap
            Output:
            - the node sifted down as far as necessary to maintain heap conditions
        '''
        
        # repeat until node is in the right position
        #   find index of a largest child
        #   if index of the largest child is not found then finish
        #   otherwise, if value of the largest child is larger than parent then swap
        
        ### WRITE YOUR CODE HERE ###

        # Set positionNotFound to True
        positionNotFound = True

        # While the position is not found
        while positionNotFound:

            # Get the largest child index
            largestChildIndex = self.__largestChild(fromIndex, last)

            # If the largest child index is None, set positionNotFound to False
            if largestChildIndex is None:
                positionNotFound = False

            # If the largest child index is larger than the parent index, swap the values
            elif self.data[largestChildIndex] > self.data[fromIndex]:

                # Swap the values, and set the fromIndex to the largestChildIndex
                # I used python's unique way of swapping values
                # This will continue the loop until the node is in the right position
                self.data[fromIndex], self.data[largestChildIndex] = self.data[largestChildIndex], self.data[fromIndex]
                fromIndex = largestChildIndex

            # Otherwise, set positionNotFound to False
            else:
                positionNotFound = False

    def sort(seq):
        
        h = Heap()
        h.buildFrom(seq)
        
        for i in range(len(seq)):
            h.data[0], h.data[h.size - 1] = h.data[h.size - 1], h.data[0]
            h.size -= 1
            h.__siftDownFromTo(0, h.size - 1)
        return h.data
        
    def __str__(self):
        st = f"\tHeap size: {(self.size)}.\n"
        st += f"\tHeap capacity: {(self.capacity)}.\n"
        st += f"\tElements of heap: \n"
        for x in range(self.size):
            st += f"\t\tValue: {(self.data[x])} at index: {x}\n"
        return st 
    def __repr__(self):
        return self.__str__()

def main():

    file = open(sys.argv[1], "r")
    for line in file:
        values = [int(x) for x in line.split()]
        
    print(f"Original list: {values}\n")

    ### WRITE YOUR CODE HERE ###

    # Create a heap object
    h = Heap()

    # Build the heap from the values
    h.buildFrom(values)

    print(f"Heapified list:\n{h}")
    
    sorted_list = Heap.sort(values)
    print(f"Sorted list: {sorted_list}")

main()

    
