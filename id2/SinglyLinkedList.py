class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList(object):
    def __init__(self):
        self.head = None

    def __len__(self):
        pre = self.head
        length = 0
        while pre:
            length += 1
            pre = pre.next
        return length

    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            pre = self.head
            while pre.next:
                pre = pre.next
            pre.next = node


if __name__ == '__main__':
    ls = LinkedList()
    ls.append(1)
    ls.append(2)
    ls.append(3)
    ls.append(4)
