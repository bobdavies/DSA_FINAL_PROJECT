"""
Binary Tree Traversal Implementation

This module implements a binary tree with various traversal methods:
- Pre-order (Root -> Left -> Right)
- In-order (Left -> Root -> Right)
- Post-order (Left -> Right -> Root)
- Level-order (Level by Level, Left to Right)

Each traversal method prints the nodes directly as they are visited.

Example:
    tree = BinaryTree()
    tree.root = TreeNode(1)
    tree.root.insert_left(2)
    tree.root.insert_right(3)
    tree.preorder_traversal(tree.root)  # Prints: 1 2 3
"""

from collections import deque
from tree_node import TreeNode

class BinaryTree:
    """
    A class implementing a binary tree with various traversal methods.
    
    The tree is built using TreeNode objects and supports four different
    traversal patterns, each printing nodes as they are visited.
    
    Attributes:
        root: Reference to the root node of the tree (TreeNode or None)
    """
    
    def __init__(self):
        """Initialize an empty binary tree."""
        self.root = None
    
    def preorder_traversal(self, node):
        """
        Perform pre-order traversal starting from the given node.
        
        Visits nodes in Root -> Left -> Right order.
        
        Args:
            node: The starting node for traversal (TreeNode or None)
        
        Example:
            tree = BinaryTree()
            tree.root = TreeNode(1)
            tree.preorder_traversal(tree.root)  # Visits root first
        """
        if node:
            print(node.value, end=" ")  # Visit root
            self.preorder_traversal(node.left)  # Traverse left
            self.preorder_traversal(node.right)  # Traverse right
    
    def inorder_traversal(self, node):
        """
        Perform in-order traversal starting from the given node.
        
        Visits nodes in Left -> Root -> Right order.
        Particularly useful for BSTs as it visits nodes in ascending order.
        
        Args:
            node: The starting node for traversal (TreeNode or None)
        
        Example:
            tree = BinaryTree()
            tree.root = TreeNode(2)
            tree.root.insert_left(1)
            tree.root.insert_right(3)
            tree.inorder_traversal(tree.root)  # Prints in sorted order: 1 2 3
        """
        if node:
            self.inorder_traversal(node.left)  # Traverse left
            print(node.value, end=" ")  # Visit root
            self.inorder_traversal(node.right)  # Traverse right
    
    def postorder_traversal(self, node):
        """
        Perform post-order traversal starting from the given node.
        
        Visits nodes in Left -> Right -> Root order.
        Useful for operations that need to process children before parents,
        such as deletion or calculating directory sizes.
        
        Args:
            node: The starting node for traversal (TreeNode or None)
        
        Example:
            tree = BinaryTree()
            tree.root = TreeNode(1)
            tree.postorder_traversal(tree.root)  # Visits root last
        """
        if node:
            self.postorder_traversal(node.left)  # Traverse left
            self.postorder_traversal(node.right)  # Traverse right
            print(node.value, end=" ")  # Visit root
    
    def levelorder_traversal(self, root):
        """
        Perform level-order traversal starting from the root.
        
        Visits nodes level by level, from left to right.
        Uses a queue to track nodes at each level.
        
        Args:
            root: The root node of the tree (TreeNode or None)
        
        Example:
            tree = BinaryTree()
            tree.root = TreeNode(1)
            tree.root.insert_left(2)
            tree.root.insert_right(3)
            tree.levelorder_traversal(tree.root)  # Prints: 1 2 3
        """
        if not root:
            return
        
        queue = deque([root])
        while queue:
            node = queue.popleft()
            print(node.value, end=" ")  # Visit node
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)