"""
Complete Binary Tree Creation Module

This module provides functionality to create a complete binary tree with 31 nodes
arranged across 4 levels. The tree is created systematically with values from 1 to 31,
assigned in a level-order fashion.

Tree Structure:
                                1
                    /                       \
                2                           3
            /       \                   /       \
          4          5                6         7
        /   \      /   \            /   \     /   \
       8     9    10    11        12    13   14   15
      / \   / \   / \   / \      / \   / \  / \   / \
    16  17 18 19 20 21 22 23    24 25 26 27 28 29 30 31

Example:
    root = create_complete_tree()
    # Creates a complete binary tree with 31 nodes
"""

from tree_node import TreeNode

def create_complete_tree():
    """
    Creates a complete binary tree with 31 nodes across 4 levels.
    
    The tree is built level by level, with values assigned from 1 to 31
    in a level-order fashion. Each non-leaf node has exactly two children.
    
    Returns:
        TreeNode: Root node of the created complete binary tree
    
    Example:
        root = create_complete_tree()
        print(root.value)  # Prints: 1
        print(root.left.value)  # Prints: 2
        print(root.right.value)  # Prints: 3
    """
    # Create root node
    root = TreeNode(1)
    
    # Level 1
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    
    # Level 2
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    
    # Level 3 - Left subtree of root.left
    root.left.left.left = TreeNode(8)
    root.left.left.right = TreeNode(9)
    root.left.right.left = TreeNode(10)
    root.left.right.right = TreeNode(11)
    
    # Level 3 - Right subtree of root.right
    root.right.left.left = TreeNode(12)
    root.right.left.right = TreeNode(13)
    root.right.right.left = TreeNode(14)
    root.right.right.right = TreeNode(15)
    
    # Level 4 - Children of nodes 8-15
    root.left.left.left.left = TreeNode(16)
    root.left.left.left.right = TreeNode(17)
    root.left.left.right.left = TreeNode(18)
    root.left.left.right.right = TreeNode(19)
    root.left.right.left.left = TreeNode(20)
    root.left.right.left.right = TreeNode(21)
    root.left.right.right.left = TreeNode(22)
    root.left.right.right.right = TreeNode(23)
    root.right.left.left.left = TreeNode(24)
    root.right.left.left.right = TreeNode(25)
    root.right.left.right.left = TreeNode(26)
    root.right.left.right.right = TreeNode(27)
    root.right.right.left.left = TreeNode(28)
    root.right.right.left.right = TreeNode(29)
    root.right.right.right.left = TreeNode(30)
    root.right.right.right.right = TreeNode(31)
    
    return root
