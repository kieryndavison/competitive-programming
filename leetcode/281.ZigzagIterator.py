class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.queue = collections.deque()
        self._insert_in_queue(iter(v1))
        self._insert_in_queue(iter(v2))
    
    def _insert_in_queue(self, cur_iter):
        try:
            self.queue.append((next(cur_iter), cur_iter))
        except StopIteration:
            pass

    def next(self) -> int:
        if self.hasNext():
            cur_val, cur_iter = self.queue.popleft()
            self._insert_in_queue(cur_iter)
            return cur_val

    def hasNext(self) -> bool:
        return len(self.queue) > 0
        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())