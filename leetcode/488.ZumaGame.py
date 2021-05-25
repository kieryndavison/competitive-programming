class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        # First make a map of the hand frequency to char
        letterCount = collections.Counter(hand)
        self.numSteps = len(hand) + 1

        # Remove groups of 3 characters
        def removeGroups(balls, limit3):
            i = 0
            for j in range(len(balls)):
                
                # while the balls are equal keep looping to find the maxium group that can be removed
                if (balls[j] == balls[i]): 
                    if not limit3: continue
                    elif j - i < 3: continue # if limit3 then restrict group size to 3
                
                # Once we find a group remove it and try again on the string with the group removed
                if j - i >= 3: return removeGroups(balls[:i] + balls[j:], limit3)
                else: i = j
            return balls
        
        # Find groups to remove
        def dfs(remaingBalls, limit3):
            
            # Remove groups and update the board string
            remaingBalls = removeGroups(remaingBalls, limit3)
            
            # if we have removed all the balls then calculate the number of steps it took 
            # (aka min of the current value for numSteps and the number of balls used from the hand)
            if remaingBalls == '#': 
                self.numSteps = min(self.numSteps, len(hand) - sum(letterCount.values()))
            i = 0
            
            for j in range(len(remaingBalls)):
                
                # if the balls are equal expand the group size
                if remaingBalls[i] == remaingBalls[j]: continue
                
                # otherwise calculate how many balls we need to use from the hand
                need = 3 - (j - i)
                
                # if we have enough balls left then we remove those balls from the hand and recurse
                if letterCount[remaingBalls[i]] >= need:
                    letterCount[remaingBalls[i]] -= need
                    dfs(remaingBalls[:i] + remaingBalls[j:], limit3)
                    letterCount[remaingBalls[i]] += need
                i = j

        dfs(board + '#', False)
        
        # if the num of steps is greater than the number of balls in the hand 
        # then try again limiting the group size to remove to 3
        if (self.numSteps > len(hand)): dfs(board + '#', True)
            
        # Return the -1 if the number of steps exceeds the number of balls 
        # in the hand, otherwise return the number of steps
        return -1 if self.numSteps > len(hand) else self.numSteps
        