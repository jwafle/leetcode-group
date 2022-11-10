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
