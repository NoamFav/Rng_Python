class ListNode:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class List:
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def append(self, value):
        new_node = ListNode(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.len += 1

    def remove(self, index):
        if index < 0 or index >= self.len:
            return

        if self.head is None:
            return

        if index == 0:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            self.len -= 1
            return

        current_node = self.head
        prev_node = None
        for i in range(index):
            prev_node = current_node
            current_node = current_node.next

        if current_node.next is None:
            self.tail = prev_node

        if prev_node is not None:
            prev_node.next = current_node.next
            self.len -= 1

    def output(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.value))
            current = current.next
        print(" -> ".join(nodes))

    def get(self, index):
        current_node = self.head
        for i in range(index):
            current_node = current_node.next
        return current_node.value

    def set(self, index, value):
        if index < 0 or index >= self.len:
            return

        current_node = self.head
        for i in range(index):
            current_node = current_node.next
        current_node.value = value

    def insert(self, index, value):
        if index < 0 or index > self.len:
            return

        new_node = ListNode(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            if self.len == 0:
                self.tail = new_node
        else:
            prev_node = None
            current_node = self.head
            for i in range(index):
                prev_node = current_node
                current_node = current_node.next

            new_node.next = current_node
            if prev_node:
                prev_node.next = new_node
            if index == self.len:
                self.tail = new_node

        self.len += 1

    def clear(self):
        self.head = None
        self.tail = None
        self.len = 0

    def getfirst(self):
        return self.head.value

    def getlast(self):
        return self.tail.value

    def setfirst(self, value):
        self.head = ListNode(value)

    def setlast(self, value):
        self.tail = ListNode(value)

    def removefirst(self):
        if not self.head:
            return
        self.head = self.head.next
        self.len -= 1
        if not self.head:
            self.tail = None

    def removelast(self):
        if self.len == 0:
            return

        if self.len == 1:
            self.head = None
            self.tail = None
        else:
            current_node = self.head
            while current_node.next is not self.tail:
                current_node = current_node.next
            current_node.next = None
            self.tail = current_node

        self.len -= 1

    def contains(self, value):
        current_node = self.head
        while current_node:
            if current_node.value == value:
                return True
            current_node = current_node.next
        return False

    def index_of(self, value):
        current_node = self.head
        index = 0
        while current_node:
            if current_node.value == value:
                return index
            index = index + 1
            current_node = current_node.next
        return False

    def reverse(self):
        # TODO: implement reverse
        pass

    def sort(self):
        # TODO: implement sort
        pass

    def min(self):
        min_value = self.head.value
        current_node = self.head
        while current_node:
            if current_node.value < min_value:
                min_value = current_node.value
            current_node = current_node.next
        return min_value

    def max(self):
        max_value = self.head.value
        current_node = self.head
        while current_node:
            if current_node.value > max_value:
                max_value = current_node.value
            current_node = current_node.next
        return max_value

    def equals(self, list2):
        # TODO: implement equals
        pass

    def get_len(self):
        return self.len


lists = List()
lists.append(1)
lists.append(2)
lists.append(3)
lists.append(4)
lists.append(5)
lists.append(6)
lists.append(7)

lists.remove(3)

lists.set(3, 127)
lists.insert(3, 376289163781)

print(lists.contains(376289163781))
print(lists.contains(1221))

lists.removelast()
lists.removefirst()

lists.append(32)

lists.append(33)

print(lists.index_of(2))

lists.output()
print(lists.get_len())
