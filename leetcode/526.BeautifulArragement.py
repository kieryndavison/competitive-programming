class Solution:
    def countArrangement(self, n: int) -> int:
        # Keep track of array permutations we have seen so far (optimization)
        self.cache = {}
        
        # Brute force try all permutations
        def dfs(pos, array):

            # if we reached the start of the array return 1
            if pos == 1: return 1

            # check if we have already tried this permuation before, 
            # if so return the total that was already calculated
            key = (pos, array)
            if key in self.cache: return self.cache[key]
            
            total = 0
            # try each value from 1 to n
            for i in range(len(array)):

                # if the current element can go in the current position 
                # then recuse on the array with the current position removed
                if pos % array[i] == 0 or array[i] % pos == 0:
                    total += dfs(pos - 1, array[:i] + array[i+1:])
            
            # update the cache after and return the total
            self.cache[key] = total
            return total
        
        # use a tuple for the array so that we can use it as a key for our cache
        return  dfs(n, tuple(range(1, n + 1)))