from typing import Any

# Binary Tree Node contains data and pointers to left and right children, and parent.


class BNode:
    Data: Any
    Parent: 'BNode'
    Left: 'BNode'
    Right: 'BNode'

    def __init__(self, data, parent, left=None, right=None):
        self.Data = data
        self.Parent = parent
        self.Left = left
        self.Right = right

# Binary Tree class contains a root node at the top and those nodes that are children of the root node to the left and right.
# A subtree is a tree that is a part of the larger tree with the parent node being the root node.
# The nodes which does not contain any children are called leaves.


class BinaryTree:
    Root: BNode

    def __init__(self):
        self.Root = BNode(data=None, parent=None, left=None, right=None)

    def Search(self, data: Any) -> BNode:
        self.__SearchNode(data=data, parentNode=self.Root)

    def Insert(self, data: Any):
        self.__InsertNode(data=data, parentNode=self.Root)
    
    def Delete(self, data: Any):
        self.__DeleteNode(data=data, parentNode=self.Root)

    # The Minimum value always in the left subtree, can be found by iteratively searching to the left. This operation is O(h) where h is the height of the tree.

    def FindMinimum(self) -> BNode:
        min = self.Root

        while (min.Left != None):
            min = min.Left

        return min

    # Similary, the Maximum value always in the right subtree.
    def FindMaximum(self) -> BNode:
        max = self.Root

        while (max.Right != None):
            max = max.Right

        return max

    # Search operation begins at the root, and then recursively searches the left and right subtrees depending on the value of the data is lager or smaller than the parent node. This operation is O(h) where h is the height of the tree.
    def __SearchNode(self, parentNode: BNode, data: Any) -> BNode:
        if parentNode is None:
            return None
        if data == None:
            return None

        if parentNode.Data == data:
            return parentNode

        if data < parentNode.Data:
            return self.__SearchNode(parentNode.Left, data)
        else:
            return self.__SearchNode(parentNode.Right, data)

    # Insert operation is similar to the search operation, but instead of returning the node, it inserts the node into the tree. This operation is O(h) where h is the height of the tree.

    def __InsertNode(self, data: Any, parentNode: BNode):
        if data == None:
            return None
        if (parentNode != None):
            if (data < parentNode.Data):
                if (parentNode.Left == None):
                    parentNode.Left = BNode(data, parentNode)
                else:
                    self.__InsertNode(data=data, parentNode=parentNode.Left)
            else:
                if (parentNode.Right == None):
                    parentNode.Right = BNode(data, parentNode)
                else:
                    self.__InsertNode(data=data, parentNode=parentNode.Right)
        else:
            pass

    # Delete a node in binary tree.
    def __DeleteNode(self, data: Any, parentNode: BNode):
        if parentNode == None:
            return parentNode

        # Finding the node to be deleted with recursion.   
        if (data < parentNode.Data):
            parentNode.Left = self.__DeleteNode(data, parentNode.Left)

        elif (data > parentNode.Data):
            parentNode.Right = self.__DeleteNode(data, parentNode.Right)

        else:
            # Handle node with only one child or no child, the successor is the child node
            if parentNode.Left == None:
                temp = parentNode.Right
                parentNode = None
            elif parentNode.Right == None:
                temp = parentNode.Left
                parentNode = None

            # Handle node with two children, the successor is the leftmost node in the right subtree
            else:
                temp = self.FindMinimum(parentNode.Right)
                parentNode.Data = temp.Data
                parentNode.Right = self.__DeleteNode(
                    temp.Data, parentNode.Right)
    
    def __TraverseInOrder(self, node: BNode):
        if node != None:
            self.__TraverseInOrder(node= node.Left)
            # Do something with the node
            self.__TraverseInOrder(node= node.Right)
