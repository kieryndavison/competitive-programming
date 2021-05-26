class Solution:
    def numDecodings(self, s: str) -> int:
        # if there are no elements in the string then it cannot be decoded 
        if s == None or len(s) == 0: return 0 
        
        # set variables to hold the last and second last totals
        n = len(s)
        prev2 = 1
        prev1 = 1 if s[0] != "0" else 0
        
        # calculate the total for the number of decodings
        for i in range(2, n + 1):
            temp = 0
            
            # if the previous character is not 0 the add the previous total to the current total
            if int(s[i-1]) != 0: temp += prev1
            
            # if the integer value of the current and previous characters is between 10 and 26 
            # (i.e. a valid character code) is not 0 the add the i - 2 total (2 times ago previous) 
            # to the current total
            if 10 <= int(s[i-2:i]) <= 26: temp += prev2
            
            # update the previous totals
            prev2 = prev1
            prev1 = temp

        # prev1 = total of all characters at the end so return it
        return prev1