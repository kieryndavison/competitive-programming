class Solution:
    # Version 1
    def countBinarySubstrings(self, s: str) -> int:
        cur, prev, res = 1, 0, 0

        # Compute the number of substrings based on the length of 
        # the current goup and the previous
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                cur += 1
            else:
                res += min(cur, prev)
                prev, cur = cur, 1
        
        return res + min(cur, prev)

    # Version 2 requires O(n) space
    def countBinarySubstrings(self, s: str) -> int:
        lengthGroups = [len(i) for i in s.replace('01', '0 1').replace('10', '1 0').split()]
        return sum(min(a, b) for a, b in zip(lengthGroups, lengthGroups[1:]))
    
    # Version 2 more readable
    def countBinarySubstrings(self, s: str) -> int:
        # Compute the length of all the groups of 1s and 0s
        groupNums = s.replace('01', '0 1').replace('10', '1 0').split()
        lengthGroups = []
        for group in groupNums:
            lengthGroups.append(len(group))
        
        # Compute the number of substrings based on the length of the groups
        ans = 0
        for len1, len2 in zip(lengthGroups, lengthGroups[1:]):
            ans += min(len1, len2)

        return ans