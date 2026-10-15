class Node:
    def __init__(self, val, key=None, next=None, prev=None):
        self.val = val
        self.key = key
        self.prev = prev
        self.next = next


class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}

        self.head = Node(0)
        self.tail = Node(0)

        self.head.next = self.tail
        self.tail.prev = self.head

        self.capacity = capacity
        self.size = 0

    def _remove_node(self, node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

        self.size -= 1

    def _insert_in_front(self, node):
        node.next = self.head.next
        node.prev = self.head

        node.next.prev = node
        self.head.next = node

        self.size += 1

    def _move_to_front(self, node):
        self._remove_node(node)
        self._insert_in_front(node)

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self._move_to_front(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._move_to_front(node)

        else:
            node = Node(val=value, key=key)

            self._insert_in_front(node)
            self.cache[key] = node

            if self.size > self.capacity:
                lru = self.tail.prev
                self._remove_node(lru)
                del self.cache[lru.key]