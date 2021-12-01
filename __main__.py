from DataStructures.LinkedList import LinkedList
from DataStructures.BinaryTree import BinaryTree

Mylist = LinkedList()
Mylist.AddToTail(data=1)
Mylist.AddToTail(data=2)
Mylist.AddToTail(data=3)
Mylist.AddToTail(data=4)

Mylist.RemoveNode(Mylist.FindNode(data=3))

Mylist.PrintList()


MyTree = BinaryTree()
MyTree.Root.Data = 1
MyTree.Insert(data=2)