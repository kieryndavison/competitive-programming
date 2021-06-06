class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        # Define dictionary to map the previous char to each char
        charPrev = {'r': 'c', 'o': 'r', 'a': 'o', 'k': 'a'}

        # Dictionary to keep track of how many of each letter we have seen
        unusedChars = {'c': 0, 'r': 0, 'o': 0, 'a': 0, 'k': 0 }

        numCroaking, maxCroaking = 0, 0
        
        # Go through the string updating the state machine and the number 
        # of frogs croaking
        for char in croakOfFrogs:
            unusedChars[char] += 1

            # If we are starting a new croak update the number of frogs that 
            # are currently croaking in additon to the max
            if char == 'c':
                numCroaking += 1
                maxCroaking = max(maxCroaking, numCroaking)
            
            # If the there are no croaks currently at the previous char then 
            # the order of the characters is not valid so return -1
            elif unusedChars[charPrev[char]] <= 0:
                return -1
            
            # Otherwise update the counter for the previous char
            else:
                unusedChars[charPrev[char]] -= 1
    
            # if we reached the end of a croak then update the number of 
            # croaks that are in progress
            if char == 'k':
                numCroaking -= 1
        
        # Return the maximum number of croaks if all croaks are complete
        return maxCroaking if numCroaking == 0 else -1
            