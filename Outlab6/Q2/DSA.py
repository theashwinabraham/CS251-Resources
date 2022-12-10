# DOCUMENTED BY: ASHWIN ABRAHAM

################################## Data Structures ################################

# ------------------------------- Singly Linked List -----------------------------

class SinglyLinkedListNode:
    '''
    This class represents each node in a singly linked list.
    Each object has attributes
        - ``data`` (The data stored in the node)
        - ``next`` (The next node in the list)

    The list of member functions are
        - ``__init__(data)`` (A constructor)
        - ``__str__()`` (converts the node object to a string)
    '''
    def __init__(self, data):
        '''
        This is a constructor for the Node object.

        :param data: Represents the data stored in the node.

        ``next`` is initialized to None.

        :return: ``None``

        :Example:
            >>> from DSA import SinglyLinkedListNode
            >>> x = SinglyLinkedListNode(3)
            >>> x.data
            3
            >>> print(x.next)
            None
        '''
        self.data = data
        self.next = None
    
    def __str__(self):
        '''
        This converts the node object to a string.
        This is done by converting the data stored in it to a string.

        :return: ``str(data)``
        :rtype: string

        :Example:
            >>> from DSA import SinglyLinkedListNode
            >>> x = SinglyLinkedListNode(3)
            >>> x.__str__()
            '3'
        '''
        return str(self.data)

class SinglyLinkedList:
    '''
    This class represents a singly linked list
    The list has attributes
        - ``head`` (representing the head of the list)
        - ``tail`` (representing the tail of the list)

    The list of available functions is
        - ``__init__()`` (A constructor for the Singly Linked List)
        - ``insert(data)`` (Inserts the given data at the tail of the list)
        - ``find(data)`` (Checks if some data is in a list and returns the node before the first instance of the node containing the given data)
        - ``deleteVal(data)`` (Deletes an instance of the given data from the Singly Linked List)
        - ``printer(sep = ', ')`` (Prints out the Singly Linked List, just like a normal Python List)
        - ``reverse()`` (Reverses the Singly Linked List)
    '''
    def __init__(self):
        '''
        This is a constructor for the Singly Linked List.


        ``head`` and ``tail`` are initialized to ``None``.

        :return: ``None``

        :Example:
            >>> from DSA import SinglyLinkedList
            >>> x = SinglyLinkedList()
            >>> print(x.head)
            None
            >>> print(x.tail)
            None
        '''
        self.head = None
        self.tail = None

    def insert(self, data):
        '''
        This inserts the given data at the tail of the list.

        :param data: Represents the data to be inserted at the tail of the list.
        :return: ``None``

        :Example:
            >>> from DSA import SinglyLinkedList
            >>> x = SinglyLinkedList()
            >>> x.insert(3)
            >>> x.head.data
            3
            >>> x.tail.data
            3
        '''
        node = SinglyLinkedListNode(data) # new node
        if not self.head: # no head
            self.head = node
        else:
            self.tail.next = node # add behind tail
        self.tail = node # move tail
    
    def find(self, data):
        '''
        This checks if some data is in a list and returns the node before the first instance of the node containing the given data.
        If the data is not present it returns the tail node.

        :param data: Represents the data that is searched for.
        :return: The node before the first instance of the node containing the given data.
        :rtype: SinglyLinkedListNode

        :Example:
            >>> from DSA import SinglyLinkedList
            >>> x = SinglyLinkedList()
            >>> x.insert(3)
            >>> x.insert(4)
            >>> x.find(4).data
            3
        '''
        head = self.head
        prev = None
        while head != None and head.data != data:
            prev = head
            head = head.next
        return prev
    
    def deleteVal(self, data):
        '''
        This deletes an instance of the given data from the Singly Linked List.
        If the data is not present in the Singly Linked List it will return False.
        Otherwise, it will delete the first instance of the node containing the given data and return True.

        :param data: Represents the data to be deleted.
        :return: True if the data is present in the list, False otherwise
        :rtype: Boolean

        :Example:
            >>> from DSA import SinglyLinkedList
            >>> x = SinglyLinkedList()
            >>> x.insert(3)
            >>> x.insert(4)
            >>> x.deleteVal(4)
            True
            >>> x.deleteVal(7)
            False
        '''
        prevPos = self.find(data)
        if prevPos.next == None:
            return False
        prevPos.next = prevPos.next.next
        return True
    
    def printer(self, sep = ', '):
        '''
        This function prints out the Singly Linked List, just like a normal Python List.

        :param sep: Represents the separator between List Elements. It's default value is ', '.
        :type sep: string
        :return: None

        :Example:
            >>> from DSA import SinglyLinkedList
            >>> x = SinglyLinkedList()
            >>> x.insert(3)
            >>> x.insert(4)
            >>> x.printer()
            [3, 4]
        '''
        ptr = self.head
        print('[', end = '')
        while ptr != None:
            print(ptr, end = '')
            ptr = ptr.next
            if ptr != None:
                print(sep, end = '')
        print(']')
    
    def reverse(self):
        '''
        This function reverses the Singly Linked List.

        :return: ``None``

        :Example:
            >>> from DSA import SinglyLinkedList
            >>> x = SinglyLinkedList()
            >>> x.insert(3)
            >>> x.insert(4)
            >>> x.reverse()
            >>> x.printer()
            [4, 3]
        '''
        head = self.head # head pointer
        prev = None # previous pointer
        while head != None: # while there is forward link left
            newHead = head.next # save extra pointer to next element
            head.next = prev # reverse the link of current element
            prev = head # move pointer to previous element
            head = newHead # use extra pointer to move to next element
        self.tail = self.head
        self.head = prev

def merge(list1, list2):
    '''
    This function merges two sorted Singly Linked Lists such that the merged list is also sorted.

    :param list1: One of the sorted lists to be merged.
    :type list1: SinglyLinkedList
    :param list2: The other sorted list to be merged.
    :type list2: SinglyLinkedList
    :return: The merged list.
    :rtype: SinglyLinkedList

    :Example:
        >>> from DSA import merge
        >>> x = SinglyLinkedList()
        >>> x.insert(3)
        >>> x.insert(4)
        >>> y = SinglyLinkedList()
        >>> y.insert(3.5)
        >>> y.insert(7)
        >>> merge(x, y).printer()
        [3, 3.5, 4, 7]
    '''
    merged = SinglyLinkedList()
    head1 = list1.head
    head2 = list2.head
    while head1 != None and head2 != None: # both lists not empty
        if head1.data < head2.data: # link node with smaller data
            merged.insert(head1.data)
            head1 = head1.next
        else:
            merged.insert(head2.data)
            head2 = head2.next
    if head1 == None and head2 != None: # list 1 finished
        merged.tail.next = head2 # add remaining list 2 as is
    if head1 != None and head2 == None: # list 2 finished
        merged.tail.next = head1 # add remaining list 1 as is
    return merged

# ------------------------------ Doubly Linked List ----------------------------

class DoublyLinkedListNode:
    '''
    This class represents each node in a doubly linked list.
    Each object has attributes
        - ``data`` (The data stored in the node)
        - ``prev`` (The previous node in the list)
        - ``next`` (The next node in the list)


    The list of available functions are
        - ``__init__(data)`` (A constructor)
        - ``__str__()`` (converts the node object to a string)
    '''
    def __init__(self, data):
        '''
        This is a constructor for the Node object.

        :param data: Represents the data stored in the node.

        ``prev`` and ``next`` are initialized to ``None``.

        :return: ``None``

        :Example:
            >>> from DSA import DoublyLinkedListNode
            >>> x = DoublyLinkedListNode(4)
            >>> x.data
            4
        '''
        self.data = data
        self.next = None
        self.prev = None
    
    def __str__(self):
        '''
        This converts the node object to a string.
        This is done by converting the data stored in it to a string.

        :return: ``str(data)``
        :rtype: string

        :Example:
            >>> from DSA import DoublyLinkedListNode
            >>> x = DoublyLinkedListNode(4)
            >>> x.__str__()
            '4'
        '''
        return str(self.data) 

class DoublyLinkedList:
    '''
    This class represents a doubly linked list
    The list has attributes
        - ``head`` (representing the head of the list)
        - ``tail`` (representing the tail of the list)

    The list of available functions is
        - ``__init__()`` (A constructor for the Doubly Linked List)
        - ``insert(data)`` (Inserts the given data at the tail of the list)
        - ``printer(sep = ', ')`` (Prints out the Doubly Linked List, just like a normal Python List)
        - ``reverse()`` (Reverses the Doubly Linked List)
    '''

    def __init__(self):
        '''
        This is a constructor for the Doubly Linked List.

        ``head`` and ``tail`` are initialized to ``None``.
        :return: ``None``
        :Example:
            >>> from DSA import DoublyLinkedList
            >>> x = DoublyLinkedList()
            >>> print(x.head)
            None
            >>> print(x.tail)
            None
        '''
        self.head = None
        self.tail = None
    
    def insert(self, data):
        '''
        This inserts the given data at the tail of the list.

        :param data: Represents the data to be inserted at the tail of the list.
        :return: ``None``

        :Example:
            >>> from DSA import DoublyLinkedList
            >>> x = DoublyLinkedList()
            >>> x.insert(3)
            >>> x.head.data
            3
            >>> x.tail.data
            3
        '''
        node = DoublyLinkedListNode(data) # new node
        if not self.head: # no head
            self.head = node
        else:
            self.tail.next = node # add behind tail
            node.prev = self.tail
        self.tail = node # move tail
    
    def printer(self, sep = ', '):
        '''
        This function prints out the Doubly Linked List, just like a normal Python List.

        :param sep: Represents the separator between List Elements. It's default value is ', '.
        :type sep: string

        :return: None

        :Example:
            >>> from DSA import DoublyLinkedList
            >>> x = DoublyLinkedList()
            >>> x.insert(3)
            >>> x.insert(4)
            >>> x.printer()
            [3, 4]
        '''
        ptr = self.head
        print('[', end = '')
        while ptr != None:
            print(ptr, end = '')
            ptr = ptr.next
            if ptr != None:
                print(sep, end = '')
        print(']')
    
    def reverse(self):
        '''
        This function reverses the Doubly Linked List.


        :return: ``None``

        :Example:
            >>> from DSA import DoublyLinkedList
            >>> x = DoublyLinkedList()
            >>> x.insert(3)
            >>> x.insert(4)
            >>> x.reverse()
            >>> x.printer()
            [4, 3]
        '''
        head = self.head # head pointer
        prev = None # previous pointer
        while head != None: # new node left
            newHead = head.next # save pointer to next node (cut forward link)
            if newHead != None: # check if next node has a reverse link
                newHead.prev = head # save pointer to previous node (cut reverse link)
            head.next = prev # reverse the forward link
            head.prev = newHead # reverse the reverse link
            prev = head # move pointer to previous element
            head = newHead # use saved pointer to move head
        self.tail = self.head
        self.head = prev

# -------------------------- Binary Search Tree ------------------------------


class BSTNode:
    '''
    This class represents each node in a Binary Search Tree.
    Each node has attributes
        - ``info`` (The data stored in the node)
        - ``left`` (The left child of the node)
        - ``right`` (The right child of the node)
        - ``level`` (The level of the node from the root)

    The member functions available are
        - ``__init__(info)`` (a constructor for the Node)
        - ``__str__()`` (converts the Node object into a string)
    '''
    def __init__(self, info):
        '''
        This is a constructor for the Node
        :param info: The data to be stored in the node
        :return: ``None``
        
        :Example:
            >>> from DSA import BSTNode
            >>> x = BSTNode(3)
            >>> x.info
            3
        '''
        self.info = info
        self.left = None
        self.right = None
        self.level = None
    
    def __str__(self):
        '''This converts the Node object into a string, by returning the string form of the data stored in the Node.

        :return: ``str(info)``
        :rtype: string

        :Example:
            >>> from DSA import BSTNode
            >>> x = BSTNode(3)
            >>> x.__str__()
            '3'
        '''
        return str(self.info)

class BinarySearchTree:
    '''
    This class represents a Binary Search Tree.
    Each object has an attribute ``root``, representing the root of the Binary Search Tree.

    The member functions available are
        - ``__init__()`` (a constructor that initializes the root to ``None``)
        - ``insert(val)`` (inserts a given value into the Binary Search Tree)
        - ``traverse(order)`` (prints out a given traversal of the Binary Search Tree)
        - ``height(root)`` (returns the height of a particular node in the Binary Search Tree from the leaves)
    '''
    def __init__(self):
        '''
        This function is a constructor that initializes the root to ``None``.
        
        
        :Example:
            >>> from DSA import BinarySearchTree
            >>> x = BinarySearchTree()
            >>> print(x.root)
            None
        '''
        self.root = None
    
    def insert(self, val):
        '''
        This function is inserts a given value into the Binary Search Tree.

        :param val: The value to be inserted in the Binary Search Tree.
        :return: ``None``

        :Example:
            >>> from DSA import BinarySearchTree
            >>> x = BinarySearchTree()
            >>> x.insert(69)
            >>> x.root.info
            69
        '''
        if self.root == None:
            self.root = BSTNode(val)
        else:
            current = self.root
            while True:
                if val < current.info: # move to left sub-tree
                    if current.left:
                        current = current.left # root moved
                    else:
                        current.left = BSTNode(val) # left init
                        break
                elif val > current.info: # move to right sub-tree
                    if current.right:
                        current = current.right # root moved
                    else:
                        current.right = BSTNode(val) # right init
                        break
                else:
                    break # value exists
    
    def traverse(self, order):
        '''This function prints out a given traversal of the Binary Search Tree.

        :param order: It can be either ``'PRE'`` (Preorder), ``'IN'`` (Inorder), ``'POST'`` (Postorder), and refers to the order in which the tree is printed
        :type order: string
        :return: ``None``

        :Example:
            >>> from DSA import BinarySearchTree
            >>> x = BinarySearchTree()
            >>> x.insert(4)
            >>> x.insert(3)
            >>> x.insert(2)
            >>> x.insert(3.5)
            >>> x.insert(5)
            >>> x.insert(7)
            >>> x.insert(6)
            >>> x.insert(8)
            >>> x.traverse('PRE')
            4 3 2 3.5 5 7 6 8 
            >>> x.traverse('IN')
            2 3 3.5 4 5 6 7 8 
            >>> x.traverse('POST')
            2 3.5 3 6 8 7 5 4 
        '''
        def preOrder(root):
            print(root.info, end = ' ')
            if root.left != None:
                preOrder(root.left)
            if root.right != None:
                preOrder(root.right)
        def inOrder(root):
            if root.left != None:
                inOrder(root.left)
            print(root.info, end = ' ')
            if root.right != None:
                inOrder(root.right)
        def postOrder(root):
            if root.left != None:
                postOrder(root.left)
            if root.right != None:
                postOrder(root.right)
            print(root.info, end = ' ')
        if order == 'PRE':
            preOrder(self.root)
        elif order == 'IN':
            inOrder(self.root)
        elif order == 'POST':
            postOrder(self.root)
    
    def height(self, root):
        '''This returns the height of a particular node in the Binary Search Tree from the leaves.

        :param root: This refers to the node whose height we're calculating
        :type root: BSTNode
        :return: The height of the given node
        :rtype: Integer

        :Example:
            >>> from DSA import BinarySearchTree
            >>> x = BinarySearchTree()
            >>> x.insert(2)
            >>> x.insert(3)
            >>> x.insert(4)
            >>> x.insert(5)
            >>> x.height(x.root.right)
            2
        '''
        if root.left == None and root.right == None:
            return 0
        elif root.right == None:
            return 1 + self.height(root.left)
        elif root.left == None:
            return 1 + self.height(root.right)
        else:
            return 1 + max(self.height(root.left),self.height(root.right))

# --------------------------------- Suffix Trie --------------------------------

class Trie:
    '''
    This is a class describing a Trie.
    The member objects in this class are
        - ``T`` (A dictionary)
    
    The member functions available are
        - ``__init__()``
        - ``find(root, c)``
        - ``insert(s)``
        - ``checkPrefix(s)``
        - ``countPrefix(s)``
    '''
    def __init__(self):
        '''
        This is a constructor that initializes the object with an empty dictionary.

        :return: ``None``

        :Example:
            >>> from DSA import Trie
            >>> x = Trie()
            >>> x.T
            {}
        '''
        self.T = {}
    
    def find(self, root, c):
        '''This function returns True if a character is in a given dictionary, else returns False

        :param root: A dictionary of character value pairs
        :type root: dictionary
        :param c: A character
        :type c: string
        :return: True if the character is in the dictionary, else returns False
        :rtype: Boolean

        :Example:
            >>> from DSA import Trie
            >>> x = Trie()
            >>> d = {}
            >>> d['a'] = {}
            >>> x.find(d, 'a')
            True
            >>> x.find(d, 'b')
            False

        '''
        return (c in root)
    
    def insert(self, s):
        '''
        This function inserts a string into the Trie

        :param s: The string to be inserted
        :type s: string
        :return: ``None``

        :Example:
            >>> from DSA import Trie
            >>> x = Trie()
            >>> x.insert('abc')
            >>> x.T
            {'a': {'#': 1, 'b': {'#': 1, 'c': {'#': 1}}}}
        '''
        root = self.T
        for c in s:
            if not self.find(root,c):
                root[c] = {}
            root = root[c]
            root.setdefault('#',0)
            root['#'] += 1
    
    def checkPrefix(self, s):
        '''Checks if the given string is a prefix of any string present in the Trie

        :param s: The string we are checking
        :type s: string
        :return: True if the given string is a prefix of any string present in the Trie, else False
        :rtype: Boolean

        :Example:
            >>> from DSA import Trie
            >>> x = Trie()
            >>> x.insert('abc')
            >>> x.checkPrefix('ab')
            True
            >>> x.checkPrefix('ac')
            False
        '''
        root = self.T
        for idx, char in enumerate(s):
            if char not in root:
                if idx == len(s) - 1:    
                    root[char] = '#'
                else:
                    root[char] = {}
            elif root[char] == '#' or idx == len(s) - 1:
                return True
            root = root[char]
        return False
    
    def countPrefix(self, s):
        '''Counts the number of strings in the Trie that have the given string as a prefix
    

        :param s: The string we are considering
        :type s: string
        :return: the number of strings in the Trie that have the given string as a prefix
        :rtype: integer
        
        :Example:
            >>> from DSA import Trie
            >>> x = Trie()
            >>> x.insert('abc')
            >>> x.insert('abcde')
            >>> x.countPrefix('ab')
            2
        '''
        found = True
        root = self.T
        for c in s:
            if self.find(root,c):
                root = root[c]
            else:
                found = False
                break
        if found:
            return root['#']
        return 0

class Heap:
    '''This class represents a heap object.

    The member functions here are:
        - ``__init__(cap)`` (A constructor)
        - ``parent(i)`` (Gives the index of the parent of an element with a given index)
        - ``left(i)`` (Gives the index of the left child of an element with a given index)
        - ``right(i)`` (Gives the index of the right child of an element with a given index)
        - ``insert(val)`` (Inserts a value in the heap)
        - ``min()`` (Returns the minimum element of the heap, if it is nonempty. It returns -1 if the heap is empty)
        - ``Heapify(root)`` (Makes a heap out of a tree whose left and right subtrees are heaps)
        - ``deleteMin()`` (Deletes the minimum element of a heap)
    '''
    def __init__(self, cap):
        '''This function is a constructor for the Heap, which initializes it with 0 elements.

        :param cap: It represents a capacity of the heap
        :return: ``None``

        :Example:
            >>> from DSA import Heap
            >>> x = Heap(5)
            >>> x.H
            [None, None, None, None, None]
            >>> x.n
            0
            >>> x.M
            5
        '''
        self.H = [None]*cap
        self.n = 0
        self.M = cap
    

    def parent(self, i):
        '''This function gives the index of the parent of an element with a given index.

        :param val: The index of the element whose parent's index we wish to find.
        :return: The index of the parent of the given element.
        :return: It returns -1 if the element is out of bound or has no parent
        :rtype: integer
        
        :Example:
            >>> from DSA import Heap
            >>> x = Heap(5)
            >>> x.parent(1)
            0
        '''
        return (i - 1) // 2
    

    def left(self, i):
        '''This function gives the index of the left child of an element with a given index.

        :param val: The index of the element whose left child's index we wish to find.
        :return: The index of the left child of the given element.
        :return: It returns -1 if the element is out of bounds or has no left child
        :rtype: integer

        :Example:
            >>> from DSA import Heap
            >>> x = Heap(5)
            >>> x.left(0)
            1
        '''
        return (2 * i) + 1


    def right(self, i):
        '''This function gives the index of the right child of an element with a given index.

        :param val: The index of the element whose right child's index we wish to find.
        :return: The index of the right child of the given element.
        :return: It returns -1 if the element is out of bounds or has no right child
        :rtype: Integer

        :Example:
            >>> from DSA import Heap
            >>> x = Heap(5)
            >>> x.right(0)
            2
        '''   
        return 2 * (i + 1)


    def insert(self, val):
        '''This function inserts a value in the heap.

        :param val: The value we wish to insert in the heap.
        
        :return: ``None``

        :Example:
            >>> from DSA import Heap
            >>> x = Heap(5)
            >>> x.insert(3)
            >>> x.H
            [3, None, None, None, None]
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

        :return: The minimum element of the heap.
        :return: -1 if the heap is empty.
        :rtype: Object

        :Example:
            >>> from DSA import Heap
            >>> x = Heap(5)
            >>> x.insert(3)
            >>> x.min()
            3
        '''   
        if (self.n != 0):
            return self.H[0]
        return -1
    

    def Heapify(self, root):
        '''This function makes a heap out of a tree whose left and right subtrees are heaps.

        :param root: The root of the heap.

        :return: ``None``

        :Example:
            >>> from DSA import Heap
            >>> x = Heap(3)
            >>> x.H = [100, 2, 3]
            >>> x.n = 3
            >>> x.Heapify(0)
            >>> x.H
            [2, 100, 3]
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
        '''
        This function deletes the minimum element of a heap.
        
        :return: ``None``

        :Example:
            >>> from DSA import Heap
            >>> x = Heap(5)
            >>> x.insert(3)
            >>> x.insert(4)
            >>> x.deleteMin()
            >>> x.min()
            4
        '''   
        if self.n > 0:
            if self.n == 1:
                self.H = []
                self.n = 0
            else:
                self.n -= 1
                self.H[0] = self.H[self.n]
                self.Heapify(0)