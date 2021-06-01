class Solution:
    # Version 1
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Set up dp array
        dp = [False] * (len(s) + 1)
        dp[0] = True

        # Convert word dictionary to a set
        words = set(wordDict)

        # Go through all the elements in the string and try each 
        # possible sub string for each element
        for i in range(1, len(s) + 1):
            for j in range(i):
                
                # If we can make s[:j] with our dictionary and s[j:i] is in our dictionary 
                # then we set dp[i] to true, since we are able to make the string up to index 
                # i using the words in the dictionary
                if dp[j] and s[j:i] in words:
                    dp[i] = True
                    break
        
        # The value of dp at the length of the string will holds whether we can make 
        # the string with words in the dictionary or not
        return dp[-1]

    # Version 2
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Set up dp array
        dp = [False] * (len(s) + 1)
        dp[0] = True

        # Convert word dictionary to a set
        words = set(wordDict)

        # Go through all the elements in the string and try each 
        # word in the dictionary for each substring
        for i in range(1, len(s) + 1):
            for word in words:
                
                # If we can make s[:i - len(word)] with our dictionary and s[i - len(word):i] 
                # is in our dictionary then we set dp[i] to true, since we are able to make 
                # the string up to index i using the words in the dictionary
                if dp[i - len(word)] and s[i - len(word):i] in words:
                    dp[i] = True
                    break
        
        # The value of dp at the length of the string will holds whether we can make 
        # the string with words in the dictionary or not
        return dp[-1]