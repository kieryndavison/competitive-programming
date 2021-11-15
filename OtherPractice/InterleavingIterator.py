import collections
class NoSuchElementException(Exception):
    pass
class IF:
    def __init__(self, iterlist):
        self.queue = collections.deque()
        for iter in iterlist:
            self._insert_in_queue(iter)
    
    def _insert_in_queue(self, cur_iter):
        try:
            self.queue.append((next(cur_iter), cur_iter))
        except StopIteration:
            pass
    
    def next(self):
        if not self.hasNext():
            raise NoSuchElementException
        cur_val, cur_iter = self.queue.popleft()
        self._insert_in_queue(cur_iter)
        return cur_val
    
    def hasNext(self):
        return len(self.queue) != 0

arr1 = [1, 2, 3]
arr2 = [4, 5]
arr3 = [6, 7, 8, 9]
a = iter(arr1)
b = iter(arr2)
c = iter(arr3)
iterlist = [a, b, c]

itfl = IF(iterlist)
while itfl.hasNext():
    print(itfl.next())
