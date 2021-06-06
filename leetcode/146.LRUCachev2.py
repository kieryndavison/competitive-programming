class Node:
    def __init__(self, val, key, next = None, prev = None):
        self.val = val
        self.key = key
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = {}
        self.tail = Node(0, 0)
        self.head = Node(0, 0)
        self.tail.prev = self.head
        self.head.next = self.tail

    def get(self, key: int) -> int:
        if key in self.dict:
            node = self.dict[key]
            self.remove(node)
            self.add(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.remove(self.dict[key])

        node = Node(value, key) 
        self.add(node)
        self.dict[key] = node

        if len(self.dict) > self.capacity:
            nodeToRemove = self.head.next
            self.remove(nodeToRemove)
            del self.dict[nodeToRemove.key]

    def remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
    
    def add(self, node):
        prev = self.tail.prev
        prev.next = node
        self.tail.prev = node
        node.prev = prev
        node.next = self.tail


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)