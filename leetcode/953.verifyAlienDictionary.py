class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # Create dictionary of the order of the letters in the language
        dictionary = {char: i for i, char in enumerate(order)}
        
        # Create a 2d array to hold the position of each character in each word
        letterOrders = [[dictionary[char] for char in word] for word in words]
        
        # Return true if all the characters in a given word are the same or come before the 
        # characters in the next word in the language otherwise return false
        return all(word1 <= word2 for word1, word2 in zip(letterOrders, letterOrders[1:]))