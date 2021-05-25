class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        if (n <= 0): return []
        
        # set up some varibles for the recursion
        totalElements = ((n - 1) * 2) + 1 
        indexMap = [False] * (n + 1)
        result = [0] * totalElements

        # try all possible options
        def createArray(index, result, indexMap):
            
            # if we have filled in all spots in the array then we are done
            if index == len(result): return True
            
            # if the array at the current index is already filled then skip to the next index
            if result[index] != 0: return createArray(index + 1, result, indexMap)
                
            # Try adding the next element to the array
            for i in range(n, 0, -1):
                if indexMap[i]: continue
                indexMap[i] = True
                result[index] = i
                
                # if we only have one spot left to fill then it must be already filled 
                # since the smallest distance between elements is 2
                if i == 1 and createArray(index + 1, result, indexMap): return True
                
                # if the element can be added to the array at a distance i from its first positon 
                # then add it and recurse on index + 1
                elif index + i < len(result) and result[index + i] == 0:
                    result[index + i] = i
                    if createArray(index + 1, result, indexMap): return True
                    result[index + i] = 0
                
                # reset values if the recursion was not successful
                result[index] = 0
                indexMap[i] = False
            
        createArray(0, result, indexMap)
        return result