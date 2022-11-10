# Data Structures

## Binary Tree

### Binary Tree as an Array
Binary trees may be represented as an array, for example:

   A
  / \
 B   C
/\   /\
D E F G

Can be stored as array:
---------------
|A|B|C|D|E|F|G|
---------------

The relationship between elements is as follows:
For node at index `i`:
Left node at `2*i`
Right node at `2*i+1`
Parent at `i/2`
