# IMPLEMENTED BY: ASHWIN ABRAHAM

class Heap:
    '''This class represents a heap object.

    The member functions here are:
        - __init__(self, cap) (A constructor)
        - parent(self, i) (Gives the index of the parent of an element with a given index)
        - left(self, i) (Gives the index of the left child of an element with a given index)
        - right(self, i) (Gives the index of the right child of an element with a given index)
        - insert(self, val) (Inserts a value in the heap)
        - min(self) (Returns the minimum element of the heap, if it is nonempty. It returns -1 if the heap is empty)
        - Heapify(self, root) (Makes a heap out of a tree whose left and right subtrees are heaps)
        - deleteMin(self) (Deletes the minimum element of a heap)
    '''
    def __init__(self, cap):
        '''This function is a constructor for the Heap, which initializes it with 0 elements.

        :param self: The class object itself
        :param cap: It represents a capacity of the heap
        '''
        self.H = [None]*cap
        self.n = 0
        self.M = cap
    

    def parent(self, i):
        '''This function gives the index of the parent of an element with a given index.

        :param self: The class object itself.
        :param val: The index of the element whose parent's index we wish to find.
        :return: The index of the parent of the given element.
        :return: It returns -1 if the element is out of bound or has no parent
        :rtype: Integer
        '''
        if i >= self.n:
            return -1
        if self.n <= 1:
            return -1
        return (i - 1) // 2
    

    def left(self, i):
        '''This function gives the index of the left child of an element with a given index.

        :param self: The class object itself.
        :param val: The index of the element whose left child's index we wish to find.
        :return: The index of the left child of the given element.
        :return: It returns -1 if the element is out of bounds or has no left child
        :rtype: Integer
        '''
        if (2*i + 1) >= self.n:
            return -1
        return (2 * i) + 1


    def right(self, i):
        '''This function gives the index of the right child of an element with a given index.

        :param self: The class object itself.
        :param val: The index of the element whose right child's index we wish to find.
        :return: The index of the right child of the given element.
        :return: It returns -1 if the element is out of bounds or has no right child
        :rtype: Integer
        '''   
        if 2*(i+1) >= self.n:
            return -1
        return 2 * (i + 1)


    def insert(self, val):
        '''This function inserts a value in the heap.

        :param self: The class object itself.
        :param val: The value we wish to insert in the heap.
        '''   
        if self.n != self.M:
            self.H[self.n] = val
            i = self.n
            self.n += 1
            while i != 0 and self.H[self.parent(i)] > self.H[i]:
                self.H[i], self.H[self.parent(i)] = self.H[self.parent(i)], self.H[i]
                i = self.parent(i)
    

    def min(self):
        '''This function returns the minimum element of the heap, if it is nonempty. It returns -1 if the heap is empty.

        :param self: The class object itself.
        :return: The minimum element of the heap.
        :return: -1 if the heap is empty.
        :rtype: Object
        '''   
        if (self.n != 0):
            return self.H[0]
        return -1
    

    def Heapify(self, root):
        '''This function makes a heap out of a tree whose left and right subtrees are heaps.

        :param self: The class object itself.
        :param root: The root of the heap.
        '''   
        l = self.left(root)
        r = self.right(root)
        s = root
        if (l < self.n and self.H[l] < self.H[root]):
            s = l
        if (r < self.n and self.H[r] < self.H[s]):
            s = r
        if s != root:
            self.H[root], self.H[s] = self.H[s], self.H[root]
            self.Heapify(s)
    

    def deleteMin(self):
        '''This function deletes the minimum element of a heap.

        :param self: The class object itself.
        '''   
        if n > 0:
            if n == 1:
                self.H = []
                n = 0
            else:
                n -= 1
                self.H[0] = self.H[n]
                self.Heapify(0)