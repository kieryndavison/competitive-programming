class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        vals = collections.Counter(changed)
        
        # special case for 0 since 0 * 2 = 0, if the number of 0 is odd then we do not have a doubled array
        if vals[0] % 2:
            return []
        
        # Go through values in sorted order so that we know that val * 2 is after val (except for 0)
        for val in sorted(vals):

            # if the number of times val appears is more than the number of times val * 2 appears, then we do not have a doubled array
            if vals[val] > vals[val * 2]:
                return []
            
            # otherwise we remove the number of times val appears from the count of val * 2 to indicate that those values have been used
            # In the case where val is 0 we remove half the number of times val appears since 0 * 2 = 0
            else:
                vals[val * 2] -= vals[val] if val else vals[val] // 2
        
        # in the end we convert the remaining values in vals back to a list and return it
        return list(vals.elements())
