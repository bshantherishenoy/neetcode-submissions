class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value 
        self.prev = None
        self.next = None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.front = Node(0,0)
        self.right =Node(0,0)
        self.front.next = self.right
        self.right.prev = self.front
        self.cache = {}
    def insert(self,node):
        pre = self.right.prev
        nxt = self.right

        pre.next = node
        node.prev = pre

        node.next = nxt
        nxt.prev = node
        
    def remove(self, node):
        pev = node.prev
        nxt = node.next
        pev.next = nxt
        nxt.prev = pev
        
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove(node)
        self.insert(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        # insert a new node
        self.cache[key]= Node(key, value)
        self.insert(self.cache[key])
        if len(self.cache) > self.capacity:
            lru = self.front.next
            self.remove(lru)
            del self.cache[lru.key]
