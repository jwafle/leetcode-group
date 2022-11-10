# 347. Top K Elements

## Definitions
Heap
: Special tree structure in which the tree is a complete binary tree

Complete Binary Tree
: A binary tree in which every level (depth), except possibly the deepest, is completely filled. At depth N, the height of the tree, all nodes must be as far left as possible

## Operations
|Operations|Description|
|----------|-----------|
|Heapify|Process of creating a heap from an array|
|Insertion|Process to insert an element in existing heap (O~(log N))|
|Deletion|Deleting the top element of the heap or the highest priority element, and then organizing the heap and returning the element with time compleixty O~(log N)|
|Peek|To check or find the most prior element in the heap, (max or min element for max and min heap)|

## Heap Types
1. Max-Heap
: In a Max-Heap the key present at the root node must be greatest among the keys present at all of it's children. The same property must be recursively true for all sub-trees in that binary tree.

2. Min-Heap
: In a Min-Heap the key present at the root node must be the minimum among the keys present at all of it's children. The same property must be recursively true for all sub-trees in that binary tree.

## Heap Applications
- Used to construct a priority queue
- Heap Sort is one of the fastest sorting algorithms with time complexity O~(N*logN), and it's easy to implement.
- Best First Search is an informed search, where the technique is implemented with a priority queue instead of a standard queue like Breadth-First Search

## Heap Real Applications
* Patient treatment: an emergency patient is treated first. Priority is the degree of injury
* Systems concerned with security use heap sort, like the Linux kernel

## Advantages
* Less time complexity for inserting or deleting an element, time complexity is O~(logN)
* It helps to find min and max number
* To just peek at the most prior element, time complexity is constant O(1)
* Can be implemented using an array, doesn't need extra space for pointer
* A binary heap is a balance binary yree, and easy to implement
* Heap can be created with O(N) time

## Disadvantages
* Time complexity for searching an element is O(N)
* To find a successor or predecessor, the heap takes O(N) time, whereas BST takes only O(log N)
* To print all elements of the heap in sorted order time complexity is O(N*logN), whereas for BST takes only O(N)
* Memory management is more complex in heap memory because it is used globally. Heap memeory is divide dinto two parts - old generations and the young generation etc. at java garbage collection
