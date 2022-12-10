/*!
 * @file DSA.h
 * @author 210050023
 * @date 28th September 2022
 * @brief Some implementations of common Data Structures and Algorithms
 * @tableofcontents
*/
#include <bits/stdc++.h>
#define ll long long int
#define vi vector<int>
#define vll vector<ll>
using namespace std;
/* ------------------------------- Data Structures ---------------------------------- */

// ------------------------------- Singly Linked List -----------------------------

/**
* @class SinglyLinkedListNode
* @brief The class for each node in a singly linked list
*/
class SinglyLinkedListNode {

    public:

        ll data; ///< A large integer to store data. This variable is public.
        SinglyLinkedListNode* next; ///< A pointer to the next node. This variable is public.
        
        /**
         * @brief Construct a new Singly Linked List Node object with next as null and data as -1
         * @param None
         */
        SinglyLinkedListNode ();
        /**
         * @brief Construct a new Singly Linked List Node object with next as null and data as -1
         * 
         * @param val (A large integer)
         */
        SinglyLinkedListNode (ll val);

};
/**
 * @brief A function that prints out the data in a node object
 * 
 * @param out (The stream)
 * @param node (The node object)
 * @return ostream& 
 */
ostream& operator<<(ostream &out, const SinglyLinkedListNode &node);
/**
* @class SinglyLinkedList
* @brief The class for a singly linked list
*/
class SinglyLinkedList {

    public:
        
        SinglyLinkedListNode *head; ///< Pointer to the head node of the list (a public variable)
        SinglyLinkedListNode *tail; ///< Pointer to the tail node of the list (a public variable)
        /**
         * @brief Constructs a new Singly Linked List object with head and tail pointers both set to null
         * @param None
         */
        SinglyLinkedList ();
        /**
         * @brief Inserts data into a linked list at the end
         * 
         * @param data (The inserted data)
         * @return void
         */        
        void insert (ll data);
        /**
         * @brief Returns a pointer to first node containing the data.
         * 
         * @param data (The data to be found)
         * @return SinglyLinkedListNode* 
         * @return tail (if the data occurs first at the tail or if it is not present at all)
         */
        SinglyLinkedListNode* find (ll data);
        /**
         * @brief Deletes a given value from a linked list.
         * 
         * @param data (value to be deleted)
         * @return true (if the data was successfully deleted)
         * @return false (if the data was not present in the list)
         */
        bool deleteVal (ll data);
        /**
         * @brief Prints out the entire singly linked list
         * 
         * @param sep An optional parameter that denotes the separater of the values. By default it is ", "
         */
        void printer (string sep = ", ");
        /**
         * @brief Reverses our list
         * 
         */
        void reverse ();

};
/**
 * @brief Merges two sorted singly linked lists and returns the new list
 * 
 * @param list1 A sorted singly linked list
 * @param list2 Another sorted singly linked list
 * @return SinglyLinkedList 
 */
SinglyLinkedList merge (SinglyLinkedList list1, SinglyLinkedList list2);

// ------------------------------- Doubly Linked List -----------------------------
/**
* @class DoublyLinkedListNode
* @brief The class for each node in a doubly linked list
*/
class DoublyLinkedListNode {

    public:
        
        ll data; ///< An integer describing the data stored in the node
        DoublyLinkedListNode *next; ///< A pointer to the next node in the Doubly Linked List
        DoublyLinkedListNode *prev; ///< A pointer to the previous node in the Doubly Linked List
        /**
         * @brief Construct a new Doubly Linked List Node object, with data set to -1 and the pointers to the previous and next nodes set to null.
         * 
         */
        DoublyLinkedListNode ();
        /**
         * @brief Construct a new Doubly Linked List Node object with pointers to the previous and next nodes set to null.
         * 
         * @param val Data to be stored in the node
         */
        DoublyLinkedListNode (ll val);

};
/**
 * @brief Prints out the data in a node
 * 
 * @param out Stream in which data is to be printed
 * @param node Node whose data is to be printed
 * @return ostream& 
 */
ostream& operator<<(ostream &out, const DoublyLinkedListNode &node);
/**
* @class DoublyLinkedList
* @brief The class for a doubly linked list
*/
class DoublyLinkedList {

    public:
        
        DoublyLinkedListNode *head; ///< A pointer to the head of the doubly linked list
        DoublyLinkedListNode *tail; ///< A pointer to the tail of the doubly linked list
        /**
         * @brief Construct a new Doubly Linked List object with the head and tail pointers initialized to null
         * 
         */
        DoublyLinkedList ();
        /**
         * @brief Inserts the given data at the tail of the Doubly Linked List
         * 
         * @param data The data to be inserted
         */
        void insert (ll data);
        /**
         * @brief Prints out the entire Doubly Linked List
         * 
         * @param sep An optional parameter that denotes the separater of the values. By default it is ", "
         */
        void printer (string sep = ", ");
        /**
         * @brief Reverses the list
         * 
         */
        void reverse ();

};

// ------------------------------- Binary Search Tree -----------------------------
/**
* @class BSTNode
* @brief The class for each node in a Binary Search Tree
*/
class BSTNode {

    public:

        ll info; ///< Data stored in the node
        ll level; ///< Level of the node (Distance from the root)
        BSTNode *left; ///< Pointer to the left child of the node
        BSTNode *right; ///< Pointer to the right child of the node
        /**
         * @brief Construct a new BSTNode object with no left or right children
         * 
         * @param val Data to be stored in the node
         */        
        BSTNode (ll val);
};
/**
 * @brief Prints out the data stored in a node
 * 
 * @param out The stream to which data is to be printed
 * @param node The node whose data is to be printed
 * @return ostream& 
 */
ostream& operator<<(ostream &out, const BSTNode &node);
/**
* @class BinarySearchTree
* @brief The class for a Binary Search Tree
*/
class BinarySearchTree {

    public:
        
        BSTNode *root; ///< A pointer to the root of the Binary Search Tree
        /**
         * @brief An enumeration of the possible orders in which the tree may be traversed
         */
        enum order {
            PRE, /*!< Preorder traversal */
            IN, /*!< Inorder traversal */
            POST /*!< Postorder traversal */
        };
        /**
         * @brief Construct a new Binary Search Tree object with no root
         * 
         */
        BinarySearchTree ();
        /**
         * @brief Inserts data in the Binary Search Tree
         * 
         * @param val Data to be inserted in the Binary Search Tree
         */
        void insert(ll val);
        /**
         * @brief traverses a Binary Search Tree in a given manner from a given node
         * 
         * @param T Node from which we start our traversal
         * @param tt Manner in which we traverse the Binary Search Tree (Preorder/Inorder/Postorder)
         */
        void traverse (BSTNode* T, order tt);
        /**
         * @brief Returns the height of a Node in a Binary Search Tree
         * 
         * @param T the Node whose height is to be found
         * @return the height
         */
        ll height(BSTNode *T);

};

// ------------------------------- Suffix Trie -----------------------------
/*!
* @class Trie
* @brief The class for a Suffix-Trie
*/
class Trie {

    public:
        
        ll count; ///< Count of nodes in the trie
        std::map<char,Trie*> nodes; ///< Dictionary of pointers to nodes with characters as keys and pointers to Tries as values
        /**
         * @brief Construct a new Trie object with no nodes and an empty Dictionary
         * 
         */
        Trie ();
        /**
         * @brief Checks if a character is present in the dictionary
         * 
         * @param T A pointer to the trie
         * @param c The character whose existence in the dictionary is to be checked
         * @return true If the character is present
         * @return false If the character is not present
         */
        bool find(Trie* T, char c);
        /**
         * @brief Inserts a string into the Suffix Trie
         * 
         * @param s The string to be inserted
         */
        void insert(string s);
        /**
         * @brief Checks if a prefix of a given string is present in our Trie
         * 
         * @param s The given string
         * @return true if any prefix of the given string is present in our Trie
         * @return false if no prefix of the given string is present in our Trie
         */
        bool checkPrefix(string s);
        /**
         * @brief Counts the number of prefixes of a given string present in our Trie
         * 
         * @param s The given string
         * @return The number of prefixes of this string
         */
        ll countPrefix(string s);

};

// ------------------------------- Heap -----------------------------
/**
 * @brief The class for a Heap
 * @class Heap
 */
class Heap {
    private:
        std::vector<ll> heap_arr; ///< The dynamic array of long integers representing the heap
    public:
        /**
         * @brief Construct a new Heap object with no elements
         * 
         */
        Heap();
        /**
         * @brief Returns the index of the parent of a particular element
         * 
         * @param i The index of the element whose parent's index we are trying to find
         * @return int
         */
        int parent(int i);
        /**
         * @brief Returns the index of the left child of an element with a given index
         * 
         * @param i The given index
         * @return int
         */
        int left(int i);
        /**
         * @brief Returns the index of the left child of an element with a given index
         * 
         * @param i The given index
         * @return int
         */
        int right(int i);
        /**
         * @brief Inserts the given value into the heap
         * 
         * @param val The value to be inserted in the heap
         */
        void insert(ll val);
        /**
         * @brief Returns the number of elements currently in the heap
         * 
         * @return long long int
         */
        ll size();
        /**
         * @brief Returns the minimum element of the heap
         * @throw "Heap Empty" Exception
         * @return long long int
         */
        ll min();
        /**
         * @brief Converts the tree rooted at a given element into a heap, given that both its left and right subtrees are already heaps
         * 
         * @param root_index The index at which the tree to be converted to a heap is rooted
         */
        void Heapify(int root_index);
        /**
         * @brief Removes the minimum element of the heap from the heap
         * @throw "Heap Empty" Exception
         */
        void deleteMin();
};