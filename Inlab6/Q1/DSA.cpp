/*!
 * @file DSA.cpp
 * @author 210050023
 * @date 21st September 2022
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
        SinglyLinkedListNode () {
            data = -1;
            next = NULL;
        }
        /**
         * @brief Construct a new Singly Linked List Node object with next as null and data as -1
         * 
         * @param val (A large integer)
         */
        SinglyLinkedListNode (ll val) {
            data = val;
            next = NULL;
        }

};
/**
 * @brief A function that prints out the data in a node object
 * 
 * @param out (The stream)
 * @param node (The node object)
 * @return ostream& 
 */
ostream& operator<<(ostream &out, const SinglyLinkedListNode &node) {
    return out << node.data;
}
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
        SinglyLinkedList () {
            head = NULL;
            tail = NULL;
        }
        /**
         * @brief Inserts data into a linked list at the end
         * 
         * @param data (The inserted data)
         * @return void
         */
        void insert (ll data) {
            SinglyLinkedListNode *node = new SinglyLinkedListNode(data);
            if (head == NULL) {
                head = node;
            }
            else {
                tail -> next = node;
            }
            tail = node;
        }
        /**
         * @brief Returns a pointer to first node containing the data.
         * 
         * @param data 
         * @return SinglyLinkedListNode* 
         * @return tail (if the data occurs first at the tail or if it is not present at all)
         */
        SinglyLinkedListNode* find (ll data) {
            SinglyLinkedListNode *ptr = head, *prev = NULL;
            while (ptr != NULL && ptr -> data != data) {
                prev = ptr;
                ptr = ptr -> next;
            }
            return prev;
        }
        /**
         * @brief Deletes a given value from a linked list.
         * 
         * @param data (value to be deleted)
         * @return true (if the data was successfully deleted)
         * @return false (if the data was not present in the list)
         */
        bool deleteVal (ll data) {
            SinglyLinkedListNode *prev = find(data);
            if (prev -> next == NULL) {
                return false;
            }
            prev -> next -> next = prev -> next;
            return true;
        }
        /**
         * @brief Prints out the entire singly linked list
         * 
         * @param sep An optional parameter that denotes the separater of the values. By default it is ", "
         */
        void printer (string sep = ", ") {
            SinglyLinkedListNode *ptr = head;
            cout << "[";
            while (ptr != NULL) {
                cout << *ptr;
                ptr = ptr -> next;
                if (ptr != NULL) {
                    cout << sep;
                }
            }
            cout << "]\n";
        }
        /**
         * @brief Reverses our list
         * 
         */
        void reverse () {
            SinglyLinkedListNode *ptr = head, *prev = NULL;
            while (ptr != NULL) {
                SinglyLinkedListNode *ptr2 = ptr -> next;
                ptr -> next = prev;
                prev = ptr;
                ptr = ptr2;
            }
            tail = ptr;
            head = prev;
        }

};
/**
 * @brief Merges two sorted singly linked lists and returns the new list
 * 
 * @param list1 A sorted singly linked list
 * @param list2 Another sorted singly linked list
 * @return SinglyLinkedList 
 */
SinglyLinkedList merge (SinglyLinkedList list1, SinglyLinkedList list2) {
    SinglyLinkedList merged;
    SinglyLinkedListNode *head1 = list1.head, *head2 = list2.head;
    while (head1 != NULL && head2 != NULL) {
        if (head1 -> data < head2 -> data) {
            merged.insert(head1 -> data);
            head1 = head1 -> next;
        }
        else {
            merged.insert(head2 -> data);
            head2 = head2 -> next;
        }
    }
    if (head1 == NULL && head2 != NULL) {
        merged.tail -> next = head2;
    }
    if (head2 == NULL && head1 != NULL) {
        merged.tail -> next = head1;
    }
    return merged;
}

// ------------------------------- Doubly Linked List -----------------------------
/**
* @class DoublyLinkedListNode
* @brief The class for each node in a doubly linked list
*/
class DoublyLinkedListNode {

    public:
        
        ll data; ///< An integer describing the data stored in the node
        DoublyLinkedListNode *next; ///< A pointer to the next node in the Doubly Linked List
        DoublyLinkedListNode* prev; ///< A pointer to the previous node in the Doubly Linked List
        /**
         * @brief Construct a new Doubly Linked List Node object, with data set to -1 and the pointers to the previous and next nodes set to null.
         * 
         */
        DoublyLinkedListNode () {
            data = -1;
            next = NULL;
            prev = NULL;
        }
        /**
         * @brief Construct a new Doubly Linked List Node object with pointers to the previous and next nodes set to null.
         * 
         * @param val Data to be stored in the node
         */
        DoublyLinkedListNode (ll val) {
            data = val;
            next = NULL;
            prev = NULL;
        }

};
/**
 * @brief Prints out the data in a node
 * 
 * @param out Stream in which data is to be printed
 * @param node Node whose data is to be printed
 * @return ostream& 
 */
ostream& operator<<(ostream &out, const DoublyLinkedListNode &node) {
    return out << node.data;
}
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
        DoublyLinkedList () {
            head = NULL;
            tail = NULL;
        }
        /**
         * @brief Inserts the given data at the tail of the Doubly Linked List
         * 
         * @param data The data to be inserted
         */
        void insert (ll data) {
            DoublyLinkedListNode *node = new DoublyLinkedListNode(data);
            if (head == NULL) {
                head = node;
            }
            else {
                tail -> next = node;
                node -> prev = tail;
            }
            tail = node;
        }
        /**
         * @brief Prints out the entire Doubly Linked List
         * 
         * @param sep An optional parameter that denotes the separater of the values. By default it is ", "
         */
        void printer (string sep = ", ") {
            DoublyLinkedListNode *ptr = head;
            cout << "[";
            while (ptr != NULL) {
                cout << *ptr;
                ptr = ptr -> next;
                if (ptr != NULL) {
                    cout << sep;
                }
            }
            cout << "]\n";
        }
        /**
         * @brief Reverses the list
         * 
         */
        void reverse () {
            DoublyLinkedListNode *ptr = head, *pr = NULL;
            while (ptr != NULL) {
                DoublyLinkedListNode *ptr2 = ptr -> next;
                if (ptr2 != NULL) {
                    ptr2 -> prev = ptr;
                }
                ptr -> next = pr;
                ptr -> prev - ptr2;
                pr = ptr;
                ptr = ptr2;
            }
            tail = ptr;
            head = pr;
        }

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
        BSTNode (ll val) {
            info = val;
            level = 0;
            left = NULL;
            right = NULL;
        }

};
/**
 * @brief Prints out the data stored in a node
 * 
 * @param out The stream to which data is to be printed
 * @param node The node whose data is to be printed
 * @return ostream& 
 */
ostream& operator<<(ostream &out, const BSTNode &node) {
    return out << node.info;
}
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
        BinarySearchTree () {
            root = NULL;
        }
        /**
         * @brief Inserts data in the Binary Search Tree
         * 
         * @param val Data to be inserted in the Binary Search Tree
         */
        void insert(ll val) {
            if (root == NULL) {
                root = new BSTNode(val);
            }
            else {
                BSTNode *ptr = root;
                while (true) {
                    if (val < ptr -> info) {
                        if (ptr -> left != NULL) {
                            ptr = ptr -> left;
                        }
                        else {
                            ptr -> left = new BSTNode(val);
                            break;
                        }
                    }
                    else if (val > ptr -> info) {
                        if (ptr -> right != NULL) {
                            ptr = ptr -> right;
                        }
                        else {
                            ptr -> right = new BSTNode(val);
                            break;
                        }
                    }
                    break;
                }
            }
        }
        /**
         * @brief traverses a Binary Search Tree in a given manner from a given node
         * 
         * @param T Node from which we start our traversal
         * @param tt Manner in which we traverse the Binary Search Tree (Preorder/Inorder/Postorder)
         */
        void traverse (BSTNode* T, order tt) {
            if (tt == PRE) {
                cout << T << endl;
                if (T -> left != NULL) {
                    traverse(T -> left,tt);
                }
                if (T -> right != NULL) {
                    traverse(T -> right,tt);
                }
            }
            else if (tt == IN) {
                if (T -> left != NULL) {
                    traverse(T -> left,tt);
                }
                cout << T << endl;
                if (T -> right != NULL) {
                    traverse(T -> right,tt);
                }
            }
            else if (tt == POST) {
                if (T -> left != NULL) {
                    traverse(T -> left,tt);
                }
                if (T -> right != NULL) {
                    traverse(T -> right,tt);
                }
                cout << T << endl;
            }
        }
        /**
         * @brief Returns the height of a Node in a Binary Search Tree
         * 
         * @param T the Node whose height is to be found
         * @return the height
         */
        ll height(BSTNode *T) {
            if (T -> left == NULL && T -> right == NULL) {
                return 0;
            }
            else if (T -> right == NULL) {
                return 1 + height(T -> left);
            }
            else if (T -> left == NULL) {
                return 1 + height(T -> right);
            }
            return max(1 + height(T -> left),1 + height(T -> right));
        }

};

// ------------------------------- Suffix Trie -----------------------------
/*!
* @class Trie
* @brief The class for a Suffix-Trie
*/
class Trie {

    public:
        
        ll count; ///< Count of nodes in the trie
        map<char,Trie*> nodes; ///< Dictionary of pointers to nodes with characters as keys and pointers to Tries as values
        /**
         * @brief Construct a new Trie object with no nodes and an empty Dictionary
         * 
         */
        Trie () {
            count = 0;
            nodes = map<char,Trie*>();
        }
        /**
         * @brief Checks if a character is present in the dictionary
         * 
         * @param T A pointer to the trie
         * @param c The character whose existence in the dictionary is to be checked
         * @return true If the character is present
         * @return false If the character is not present
         */
        bool find(Trie* T, char c) {
            return ((T -> nodes).find(c) != (T -> nodes).end());
        }
        /**
         * @brief Inserts a string into the Suffix Trie
         * 
         * @param s The string to be inserted
         */
        void insert(string s) {
            Trie* ptr = this;
            for (auto c: s) {
                if (!find(ptr,c)) {
                    (ptr -> nodes)[c] = new Trie();
                }
                ptr = (ptr -> nodes)[c];
                (ptr -> count)++;
            }
        }
        /**
         * @brief Checks if a prefix of a given string is present in our Trie
         * 
         * @param s The given string
         * @return true if any prefix of the given string is present in our Trie
         * @return false if no prefix of the given string is present in our Trie
         */
        bool checkPrefix(string s) {
            Trie* ptr = this;
            for (ll i = 0; i < s.length(); i++) {
                if (!find(ptr,s[i])) {
                    if (i == s.length() - 1) {
                        (ptr -> nodes)[s[i]] = NULL;
                    }
                    else {
                        (ptr -> nodes)[s[i]] = new Trie();
                    }
                }
                else if ((ptr -> nodes)[s[i]] == NULL or i == s.length() - 1) {
                    return true;
                }
                ptr = (ptr -> nodes)[s[i]];
            }
            return false;
        }
        /**
         * @brief Counts the number of prefixes of a given string present in our Trie
         * 
         * @param s The given string
         * @return The number of prefixes of this string
         */
        ll countPrefix(string s) {
            bool found = true;
            Trie* ptr = this;
            for (auto c: s) {
                if (find(ptr,c)) {
                    ptr = (ptr -> nodes)[c];
                }
                else {
                    found = false;
                    break;
                }
            }
            if (found) {
                return ptr -> count;
            }
            return 0;
        }

};

/*!
* @class Heap
* @brief This class is used to represent a min heap
*/
class Heap
{
    public:
        vector<ll> arr; ///< Dynamic Array representing the heap

        /**
         * @brief Returns the index of the parent of the element with the given index
         * 
         * @param i The index of the element
         * @return index
         * @return -1 if the input index is out of bounds or the element corresponding to it has no parent
         */
        int parent(int i)
        {
            if(i <=0 || i>= arr.size()) return -1;
            return (i-1)/2;
        }

        /**
         * @brief Returns the index of the left child of the element with the given index
         * 
         * @param i The index of the element
         * @return index
         * @return -1 if the input index is out of bounds or the element corresponding to it has no left child
         */
        int left(int i)
        {
            if(2*i + 1 >= arr.size()) return -1;
            return 2*i + 1;
        }

        /**
         * @brief Returns the index of the right child of the element with the given index
         * 
         * @param i The index of the element
         * @return index
         * @return -1 if the input index is out of bounds or the element corresponding to it has no right child
         */
        int right(int i)
        {
            if(2*(i+1) >= arr.size()) return -1;
            return 2*(i+1);
        }

        /**
         * @brief Returns the smallest element in the heap
         * 
         * @return Returns the smallest element in the heap
         * @return -1 if the heap is empty
         *
         */
        ll min()
        {
            if(arr.size() == 0) return -1;
            return arr[0];
        }
};