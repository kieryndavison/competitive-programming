class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # set up variables to keep track of the max length, start index 
        # and a map to map the characters we have seen so far to their index
        start, maxLen = 0, 0
        mapIndex = {}
        
        for i in range(len(s)):

            # if the current value has been seen before and its index is 
            # within the window then update the max length and update the 
            # start of the window to be one after the matching element
            if s[i] in mapIndex and mapIndex[s[i]] >= start:
                maxLen = max(maxLen, i - start)
                start = mapIndex[s[i]] + 1
            
            # add each element we see to the map, with its value being its most recent index
            mapIndex[s[i]] = i

        # handle the case were the longest substring goes to the end of the array
        return max(maxLen, len(s) - start)