from DataStructures.LinkedList import LinkedList
from DataStructures.BinaryTree import BinaryTree
from DataStructures.Graph import Graph

# Linked List Test
Mylist = LinkedList()
Mylist.AddToTail(data=1)
Mylist.AddToTail(data=2)
Mylist.AddToTail(data=3)
Mylist.AddToTail(data=4)

Mylist.RemoveNode(Mylist.FindNode(data=3))
Mylist.PrintList()

# Binary Tree Test
MyTree = BinaryTree()
MyTree.Root.Data = 1
MyTree.Insert(data=2)

# Graph (adjacency list) Test
myGraph = Graph()
myGraph.read_graph()
'''
Input:
Enter the number of vertices: 4
Enter the number of edges: 4
Enter the edge (x, y , weight): 1 0 0 
Enter the edge (x, y , weight): 2 0 0
Enter the edge (x, y , weight): 3 0 0
Enter the edge (x, y , weight): 1 3 0

Output:
Vertex:  0 -> 3 (0) -> 2 (0) -> 1 (0)
Vertex:  1 -> 3 (0)
Vertex:  2
Vertex:  3 -> 1 (0)

Graph will be like this:
0-1
|\|
2 3
'''
myGraph.print_graph()