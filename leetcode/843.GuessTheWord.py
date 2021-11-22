# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        matches = 0
        
        # keep guessing until we get a match
        while matches < 6:
            count_letter = []

            # Create an array which contains a dictionary of the number of times a 
            # character occurs in that position accross all words in the wordlist
            for i in range(6):
                count_letter.append(collections.Counter(word[i] for word in wordlist))
             
            # Find the word that has the most overlaping letters with other words
            guess = wordlist[0]
            max_score = 0
            for word in wordlist:
                word_sum = sum(count_letter[i][char] for i, char in enumerate(word))
                
                if word_sum > max_score:
                    guess = word
                    max_score = word_sum
            
            matches = master.guess(guess)
            wordlist2 = []

            # After guessing a word update the wordlist to only contain words that 
            # have the same number of matches with the current word as the secrete word
            for word in wordlist:
                if self.match(word, guess) == matches:
                    wordlist2.append(word)
            
            wordlist = wordlist2
    
    # helper function which determines the number of characters that match between two words
    def match(self, word1, word2):
            return sum(i == j for i, j in zip(word1, word2))           
            