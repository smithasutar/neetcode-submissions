class Node:
    def __init__(self, key: int, value: int, next: 'Node' = None):
        self.key = key
        self.value = value
        self.next = self.prev = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        
        self.left.next = self.right
        self.right.prev = self.left
    
    def insert(self, node):
        back = self.right.prev
        front = self.right
        back.next = node
        front.prev = node
        node.next = front
        node.prev = back

    def remove(self, node):
        back = node.prev
        front = node.next
        back.next = front
        front.prev = back

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]


