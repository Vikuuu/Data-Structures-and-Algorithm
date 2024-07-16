class LinkNode:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.next = nextNode


class MyLinkedList:

    def __init__(self):
        self.head = LinkNode(0)
        self.tail = self.head
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index > self.size:
            return -1

        curr = self.head.next
        for _ in range(index):
            curr = curr.next

        return curr.value if curr else -1

    def addAtHead(self, val: int) -> None:
        self.size += 1
        new_node = LinkNode(val)
        new_node.next = self.head.next
        self.head.next = new_node
        if not new_node.next:
            self.tail = new_node

        # or can use
        # addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.size += 1
        self.tail.next = LinkNode(val)
        self.tail = self.tail.next

        # or can use
        # addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return

        self.size += 1
        pred = self.head
        for _ in range(index):
            pred = pred.next

        new_node = LinkNode(val)
        new_node.next = pred.next
        pred.next = new_node
        if pred == self.tail:
            self.tail = pred.next

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        pred = self.head
        for _ in range(index):
            pred = pred.next
        if pred.next == self.tail:
            self.tail = pred
        pred.next = pred.next.next
        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
