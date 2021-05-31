class Solution:
    def validPalindrome(self, s: str) -> bool:
        # Use normal 2 pointer solution palindrome but if we find a mismatch, 
        # then we try removing either the left or right element and if that 
        # string is a palindrome (i.e. equal to its reverse) then we return true

        left, right = 0, len(s) - 1
        while left <= right:
            if s[left] != s[right]:
                removeLeft, removeRight = s[left + 1:right + 1], s[left:right]
                return removeLeft == removeLeft[::-1] or removeRight == removeRight[::-1]
            left, right = left + 1, right - 1
        return True