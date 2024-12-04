# Binary Tree Traversals Implementation

This project implements comprehensive binary tree traversal algorithms in Python, featuring four different traversal methods: pre-order, in-order, post-order, and level-order. The implementation includes a visual representation of the tree structure and demonstrates each traversal's unique pattern through a complete binary tree.

## Problem Description

Binary tree traversal is a fundamental operation in computer science that involves visiting each node in a binary tree exactly once in a specific order. The project implements four classic traversal methods:

1. Pre-order: Visit root, then traverse left subtree, then right subtree
2. In-order: Traverse left subtree, visit root, then traverse right subtree
3. Post-order: Traverse left subtree, traverse right subtree, then visit root
4. Level-order: Visit nodes level by level, from left to right

## Project Structure

The project is organized into four Python files:

1. `tree_node.py`: Defines the basic tree node structure
2. `tree_traversals.py`: Implements all traversal algorithms
3. `create_tree.py`: Builds the complete binary tree
4. `main.py`: Orchestrates the demonstration of all traversals

### Tree Node Implementation (`tree_node.py`)

The TreeNode class provides the fundamental building block for the binary tree:

```python
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
```

Key methods:

- `insert_left(child)`: Add a left child node
- `insert_right(child)`: Add a right child node

### Binary Tree Implementation (`tree_traversals.py`)

The BinaryTree class implements all traversal algorithms:

```python
class BinaryTree:
    def __init__(self):
        self.root = None
```

Key features:

- Recursive implementation for depth-first traversals
- Queue-based implementation for level-order traversal
- Direct printing of nodes with consistent formatting
- Clear separation of traversal logic

### Tree Creation Implementation (`create_tree.py`)

The create_tree module builds a complete binary tree with 31 nodes:

```python
from tree_node import TreeNode

def create_complete_tree():
    """
    Creates a complete binary tree with 31 nodes (4 levels)
    Returns the root node of the tree
    """
    root = TreeNode(1)
    # Level 1
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    # Level 2, etc...
```

Key features:

- Creates a complete binary tree systematically
- Uses TreeNode class for node creation
- Implements a clear node numbering system (1 to 31)
- Maintains balanced tree structure

### Main Program Implementation (`main.py`)

The main module orchestrates the tree creation and traversal demonstrations:

```python
from tree_traversals import BinaryTree
from create_tree import create_complete_tree

def display_traversals():
    """
    Creates a binary tree and displays all traversal orders
    """
    # Create and setup the binary tree
    tree = BinaryTree()
    tree.root = create_complete_tree()
    
    # Display all traversals with proper formatting
    print("\nBinary Tree Traversals")
    print("=============================")
    # ... traversal demonstrations ...
```

Key features:

- Integrates all components (TreeNode, BinaryTree, tree creation)
- Provides formatted output for all traversals
- Serves as the entry point for the program
- Includes descriptive headers and clear output formatting

## Tree Structure

The implementation uses a complete binary tree with 31 nodes across 4 levels:

```
                                1
                    /                       \
                2                           3
            /       \                   /       \
          4          5                6         7
        /   \      /   \            /   \     /   \
       8     9    10    11        12    13   14   15
      / \   / \   / \   / \      / \   / \  / \   / \
    16  17 18 19 20 21 22 23    24 25 26 27 28 29 30 31
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/DSA_FINAL_PROJECT.git
cd DSA_FINAL_PROJECT/tree_traversals
```

2. Ensure you have Python 3.x installed:

```bash
python --version
```

The implementation uses only Python's standard library (collections.deque for level-order traversal).

## Usage

1. Run the program:

```bash
python main.py
```

2. The program will:
   - Create a complete binary tree with 31 nodes
   - Demonstrate all four traversal methods
   - Display formatted output for each traversal

## Output Examples

### 1. Pre-order Traversal

```
Pre-order Traversal (Root -> Left -> Right):
1 2 4 8 16 17 9 18 19 5 10 20 21 11 22 23 3 6 12 24 25 13 26 27 7 14 28 29 15 30 31
```

### 2. In-order Traversal

```
In-order Traversal (Left -> Root -> Right):
16 8 17 4 18 9 19 2 20 10 21 5 22 11 23 1 24 12 25 6 26 13 27 3 28 14 29 7 30 15 31
```

### 3. Post-order Traversal

```
Post-order Traversal (Left -> Right -> Root):
16 17 8 18 19 9 4 20 21 10 22 23 11 5 2 24 25 12 26 27 13 6 28 29 14 30 31 15 7 3 1
```

### 4. Level-order Traversal

```
Level-order Traversal (Level by Level):
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31
```

## Algorithm Details

### Depth-First Traversals

- Pre-order, In-order, and Post-order use recursive algorithms
- Time Complexity: O(n) where n is the number of nodes
- Space Complexity: O(h) where h is the height of the tree
  - Best case (balanced): O(log n)
  - Worst case (skewed): O(n)

### Level-Order Traversal

- Uses a queue-based iterative algorithm
- Time Complexity: O(n)
- Space Complexity: O(w) where w is the maximum width of the tree
  - For a complete binary tree: O(n/2) ≈ O(n)

## Implementation Features

### TreeNode Class

- Defined in `tree_node.py`
- Properties:
  - value: Node's data
  - left: Reference to left child
  - right: Reference to right child
- Methods for child node insertion

### BinaryTree Class

- Defined in `tree_traversals.py`
- Methods:
  - preorder_traversal(node)
  - inorder_traversal(node)
  - postorder_traversal(node)
  - levelorder_traversal(root)
- Direct printing with consistent formatting

## Contributing

Contributions are welcome! Some potential areas for enhancement:

- Adding tree visualization using graphics libraries
- Implementing iterative versions of recursive traversals
- Adding more tree operations (insertion, deletion, search)
- Creating an interactive mode for building custom trees
- Adding unit tests and documentation

## License

This project is open source and available under the MIT License.
