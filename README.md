# Binary Search Tree (BST)

###### Technologies:
<p align="center">
<img src="https://img.icons8.com/color/75/000000/python.png" width="75" height="75" alt="Python" style="margin: 10px 15px 0 15px;" />
</p>

### Try it!

To run the Binary Search Tree application, follow the instructions in the Setup section below.

## Project Structure

- `binary_search_tree.py`: Contains the implementation of the Binary Search Tree (BST) class and functions.

## Setup

### Prerequisites

- Python 3 installed

### Installation Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/creinis/binary-search-tree-bst-fcc-scicomp-py-cert.git
   cd binary-search-tree-fcc-scicomp-py-cert
   ```

2. Run the Binary Search Tree script:
   ```bash
   python3 binary_search_tree.py
   ```

## Binary Search Tree (BST)

### Functionality

The Binary Search Tree (BST) is a data structure that facilitates fast lookup, addition, and deletion operations. Nodes in the BST are arranged in such a way that for any given node, the left subtree contains nodes with keys less than the node's key, and the right subtree contains nodes with keys greater than the node's key.

### Practical Use Case

The Binary Search Tree is useful for various applications such as database indexing, searching large datasets, and implementing associative arrays. It is particularly efficient for scenarios where data is dynamically changing and fast search, insert, and delete operations are required.

### Benefits

- **Efficiency:** Provides average-case time complexity of O(log n) for search, insert, and delete operations.
- **Dynamic Data:** Suitable for applications with dynamic datasets that frequently change.
- **Structured Storage:** Maintains a sorted order of elements, facilitating in-order traversal to retrieve data in sorted order.
- **Python Standard Library:** Utilizes Python’s built-in data structures for implementation.

## How to Use

1. Run the `binary_search_tree.py` script:
   ```bash
   python3 binary_search_tree.py
   ```

2. The `BinarySearchTree` class can be used to create a BST and perform various operations such as insertion, search, and deletion.

### Example Usage

```python
from binary_search_tree import BinarySearchTree

# Create a new Binary Search Tree
bst = BinarySearchTree()

# Insert nodes into the BST
nodes = [50, 30, 20, 40, 70, 60, 80]
for node in nodes:
    bst.insert(node)

# Perform in-order traversal
print("Inorder traversal:", bst.inorder_traversal())

# Search for a node
print("Search for 40:", bst.search(40))

# Delete a node
bst.delete(40)
print("Inorder traversal after deleting 40:", bst.inorder_traversal())
print("Search for 40:", bst.search(40))
```

### Example Output

```plaintext
Inorder traversal: [20, 30, 40, 50, 60, 70, 80]
Search for 40: <TreeNode object with key 40>
Inorder traversal after deleting 40: [20, 30, 50, 60, 70, 80]
Search for 40: None
```

## Function Parameters

- `key`: The key value to insert, search, or delete in the BST.

### Constraints

- The keys should be comparable elements (e.g., all integers or all floats).

### Additional Information

- **Insertion:** Inserts a new node in the correct position to maintain BST properties.
- **Search:** Finds and returns the node with the specified key.
- **Deletion:** Removes a node with the specified key and reorganizes the tree to maintain BST properties.
- **Traversal:** Performs an in-order traversal of the BST to retrieve elements in sorted order.

---
#### This is a FreeCodeCamp Challenge for Scientific Computing with Python Projects Certification.
<p align="center">
<img src="https://cdn.freecodecamp.org/platform/universal/fcc_primary.svg" width="250" height="75" alt="freeCodeCamp" style="margin: 0 15px; opacity: 0.6" />
</p>
