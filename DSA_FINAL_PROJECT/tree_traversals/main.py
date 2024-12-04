"""
Binary Tree Traversals - Main Program

This module serves as the entry point for demonstrating various binary tree
traversal methods. It creates a complete binary tree with 31 nodes and
demonstrates four different traversal patterns:
1. Pre-order (Root -> Left -> Right)
2. In-order (Left -> Root -> Right)
3. Post-order (Left -> Right -> Root)
4. Level-order (Level by Level)

Example:
    To run the demonstration:
    $ python main.py

Output Format:
    Binary Tree Traversals
    =============================
    Tree with 31 nodes (4 levels)

    1. Pre-order Traversal:
    1 2 4 8 16 17 9 18 19 5 ...

    2. In-order Traversal:
    16 8 17 4 18 9 19 2 20 ...
    
    ... etc.
"""

from tree_traversals import BinaryTree
from create_tree import create_complete_tree

def display_traversals():
    """
    Creates a binary tree and demonstrates all traversal methods.
    
    This function:
    1. Creates a complete binary tree with 31 nodes
    2. Displays the tree structure information
    3. Demonstrates all four traversal methods with formatted output
    
    The output is formatted with clear headers and proper spacing
    to make the traversal patterns easily readable.
    
    Example:
        display_traversals()
        # Outputs all traversals with proper formatting
    """
    # Create and setup the binary tree
    tree = BinaryTree()
    tree.root = create_complete_tree()
    
    # Display tree structure information
    print("\nBinary Tree Traversals")
    print("=============================")
    print("Tree with 31 nodes (4 levels)")
    
    # Demonstrate pre-order traversal
    print("\n1. Pre-order Traversal (Root -> Left -> Right):")
    print(" ", end="")
    tree.preorder_traversal(tree.root)
    print()  # New line after traversal
    
    # Demonstrate in-order traversal
    print("\n2. In-order Traversal (Left -> Root -> Right):")
    print(" ", end="")
    tree.inorder_traversal(tree.root)
    print()  # New line after traversal
    
    # Demonstrate post-order traversal
    print("\n3. Post-order Traversal (Left -> Right -> Root):")
    print(" ", end="")
    tree.postorder_traversal(tree.root)
    print()  # New line after traversal
    
    # Demonstrate level-order traversal
    print("\n4. Level-order Traversal (Level by Level):")
    print(" ", end="")
    tree.levelorder_traversal(tree.root)
    print()  # New line after traversal

if __name__ == "__main__":
    display_traversals()
