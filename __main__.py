from DataStructures.LinkedList import LinkedList

Mylist = LinkedList()
Mylist.AddToTail(data=1)
Mylist.AddToTail(data=2)
Mylist.AddToTail(data=3)
Mylist.AddToTail(data=4)

Mylist.RemoveNode(Mylist.FindNode(data=3))

Mylist.PrintList()