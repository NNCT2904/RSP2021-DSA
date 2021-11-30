from typing import Any

class Node:
    def __init__(self, data=None, next=None):
        self.Data = data
        self.Next = next


class LinkedList:
    Head: Node
    Tail: Node

    def __init__(self):
        self.Head = Node(data=None, next=None)
        self.Tail = Node(data=None, next=None)
        self.Head.Next = self.Tail

    def AddAfter(self, data: Any, previous: Node):
        newNode = Node(data=data)
        newNode.Next = previous.Next
        previous.Next = newNode

        return newNode

    def AddToTail(self, data: Any):
        currentNode = self.Head
        while(currentNode.Next != self.Tail):
            currentNode = currentNode.Next

        self.AddAfter(data=data, previous=currentNode)

    def PrintList(self):
        currentNode = self.Head.Next
        if (currentNode.Next != self.Tail):
            print('The List contains:', end=' ')
            while (currentNode != self.Tail):
                print(currentNode.Data, end=' ')
                currentNode = currentNode.Next
            print()
        else:
            print('The list is empty')