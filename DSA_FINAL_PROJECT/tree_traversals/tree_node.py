"""
TreeNode Class - Basic Building Block for Binary Tree Implementation

This module provides the TreeNode class, which represents a single node in a binary tree.
Each node contains a value and references to its left and right children.

Example:
    node = TreeNode(5)
    node.insert_left(3)
    node.insert_right(7)
"""

class TreeNode:
    """
    A class representing a node in a binary tree.
    
    Each node has a value and can have left and right children.
    The children can be None, indicating no child in that position.
    
    Attributes:
        value: The data stored in the node
        left: Reference to the left child node (TreeNode or None)
        right: Reference to the right child node (TreeNode or None)
    """
    
    def __init__(self, value):
        """
        Initialize a new TreeNode with the given value.
        
        Args:
            value: The data to be stored in the node
        """
        self.value = value
        self.left = None
        self.right = None
    
    def insert_left(self, child):
        """
        Insert a left child node.
        
        Args:
            child: TreeNode to be inserted as the left child
        """
        if self.left is None:
            self.left = child
        else:
            child.left = self.left
            self.left = child
            
    def insert_right(self, child):
        """
        Insert a right child node.
        
        Args:
            child: TreeNode to be inserted as the right child
        """
        if self.right is None:
            self.right = child
        else:
            child.right = self.right
            self.right = child
