class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        dictionary = defaultdict(list)
        
        # Make a dictionary mapping parent processes to their direct child processes
        for c, p in zip(pid, ppid):
            if p > 0:
                dictionary[p].append(c)
        
        queue = deque([kill])
        res = []

        # BFS, adding list of child processes for each process in the queue
        while queue:
            curPid = queue.popleft()
            res.append(curPid)
            
            if curPid in dictionary:
                for p in dictionary[curPid]:
                    queue.append(p)
        
        return res