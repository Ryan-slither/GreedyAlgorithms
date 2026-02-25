from dataclasses import dataclass


@dataclass
class InputData:
    cache_size: int
    requests_count: int
    requests: list[int]


@dataclass
class OutputData:
    FIFO_misses: int
    LRU_misses: int
    OPTFF_misses: int


@dataclass
class Node:
    value: object
    prev: "Node | None" = None
    next: "Node | None" = None


class DoublyLinkedList:
    def __init__(self):
        self.head: "Node | None" = None
        self.tail: "Node | None" = None

    def append(self, value: object) -> Node:
        newNode: Node
        if self.tail is None:
            newNode = Node(value, None, None)
            self.tail = newNode
            self.head = newNode
        else:
            prev = self.tail
            newNode = Node(value, prev, None)
            self.tail.next = newNode
            self.tail = newNode

        return newNode

    def popLeft(self) -> Node | None:
        if self.head is None:
            return

        returned = self.head
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            nextHead = self.head.next
            # nextHead.prev will never be None in this case because there is more than one node guarenteed
            nextHead.prev = None  # type: ignore
            self.head = nextHead

        return returned

    def popRight(self):
        if self.tail is None:
            return

        if self.head == self.tail:
            self.head = None
            self.tail = None
            return

        nextTail = self.tail.prev
        # nextTail.prev will never be None in this case because there is more than one node guarenteed
        nextTail.next = None  # type: ignore
        self.tail = nextTail

    def remove(self, node: Node):
        if node == self.head:
            self.popLeft()
        elif node == self.tail:
            self.popRight()
        else:
            prevNode = node.prev
            nextNode = node.next
            # There is guarenteed to be at least three nodes at this point so accessing is safe
            prevNode.next = nextNode  # type: ignore
            nextNode.prev = prevNode  # type: ignore

    def printForward(self):
        print("Forward:")
        curr = self.head
        while curr is not None:
            print(curr.value)
            curr = curr.next
        print()

    def printBackward(self):
        print("Backward:")
        curr = self.tail
        while curr is not None:
            print(curr.value)
            curr = curr.prev
        print()
