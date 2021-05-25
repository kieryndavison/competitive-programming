class Node:
    def __init__(self, data, key) -> None:
        self.val = data
        self.key = key
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
    
    # Define delete operation for the linked list
    def delete(self, delNode: Node):
        # skip if head or node is none
        if self.head is None or delNode is None: return
        
        # Reset the tail if we are deleting it
        if delNode == self.tail: self.tail = self.tail.prev
        
        # Reset the head if we are deleting it
        if delNode == self.head: self.head = self.head.next
        
        # update the prev and next pointers of the prev and next elements if they exisit
        if delNode.next is not None: delNode.next.prev = delNode.prev
        if delNode.prev is not None: delNode.prev.next = delNode.next

    # Define push operation for the linked list
    def push(self, newNode):
        # set the next element to be the head of the list
        newNode.next = self.head

        # update the old head elements previous if it exisits
        if self.head is not None: self.head.prev = newNode
            
        # update the tail if it is not set
        if self.tail is None: self.tail = newNode

        # set the new node to be the head element and reset its previous pointer
        self.head = newNode
        self.head.prev = None


class LRUCache:

    # initialize the a doubly linked list, dictionary and capacity for the cache
    def __init__(self, capacity: int):
        self.dll = DoublyLinkedList()
        self.map = {}
        self.capacity = capacity

    # return -1 if the element is not found, otherwise move the element to the front of the list
    def get(self, key: int) -> int:
        if key not in self.map: return -1
        newNode = self.map[key]
        self.dll.delete(newNode)
        self.dll.push(newNode)
        return newNode.val

    # insert the key and value to the map and linked list or update the value if the key already exisits
    def put(self, key: int, value: int) -> None:
        
        # if the key has already been inserted then delete it
        if key in self.map:
            self.dll.delete(self.map[key])
        
        # add the new pair to the map and linked list
        self.dll.push(Node(value, key))
        self.map[key] = self.dll.head
        
        # remove the least recently used element (last element in the linked list) if we are over capacity 
        if len(self.map) > self.capacity: 
            node = self.dll.tail
            self.dll.delete(node)
            del self.map[node.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)