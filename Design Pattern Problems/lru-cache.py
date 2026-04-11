class Node:

    def __init__(self, key: int = 0, val: int = 0):
        self.val = val
        self.key = key
        self.next: Node = None
        self.prev: Node = None
    
    def __str__(self) -> str:
         return f"Node(key={self.key}, val={self.val})"

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.cache: return -1
        node = self.cache[key]
        self.removeNode(node)
        self.insertFront(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.removeNode(node)
            self.insertFront(node)
            return

        node = Node(key, value)
        self.cache[key] = node
        self.insertFront(node)

        if len(self.cache) > self.capacity:
            node = self.tail.prev
            rmKey = node.key
            self.removeNode(node)
            del self.cache[rmKey]

    def insertFront(self, node: Node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
