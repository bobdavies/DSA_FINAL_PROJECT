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
    
    def insert_left(self, value):
        """
        Insert a left child node.
        
        Args:
            value: Either a value to create a new node with, or an existing TreeNode
        
        Returns:
            TreeNode: The inserted left child node
        
        Example:
            node = TreeNode(5)
            left_child = node.insert_left(3)
        """
        if isinstance(value, TreeNode):
            self.left = value
        else:
            self.left = TreeNode(value)
        return self.left
    
    def insert_right(self, value):
        """
        Insert a right child node.
        
        Args:
            value: Either a value to create a new node with, or an existing TreeNode
        
        Returns:
            TreeNode: The inserted right child node
        
        Example:
            node = TreeNode(5)
            right_child = node.insert_right(7)
        """
        if isinstance(value, TreeNode):
            self.right = value
        else:
            self.right = TreeNode(value)
        return self.right
