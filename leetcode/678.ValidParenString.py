class Solution:
    def checkValidString(self, s: str) -> bool:
        # variables to hold the max and min amounts of ) needed
        cmax = cmin = 0
        
        for char in s:
            
            # if the character is a ) then we know that we will need one less ) 
            # otherwise we could have one more (since * can be either '(' or ')')
            cmax = cmax - 1 if char == ')' else cmax + 1
            
            # similarly if the character is a ( then we know that we will need one more ) 
            # otherwise need one less, to a minimum of 0
            cmin = cmin + 1 if char == '(' else max(cmin - 1, 0)
            
            # if we have more ) than ( at any point we know that the string cannot be valid
            # therefore we can return false immediately
            if cmax < 0: return False

        # if at a minimum there are no more ) required to make the string valid then it is valid
        return cmin == 0