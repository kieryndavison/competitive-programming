class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        num_letters = 0
        cur_words = []
        res = []
        for word in words:
            # if we adding another word would go over the max length then create a line
            if num_letters + len(cur_words) + len(word) > maxWidth:
                num_spaces = max(len(cur_words) - 1, 1) # handle the case where there is only one word
                
                # distribute spaces using round robbin method - ensure that an extra spaces are put on the left
                for i in range(maxWidth - num_letters):
                    cur_words[i % num_spaces] += ' '
            
                res.append("".join(cur_words))
                num_letters = 0
                cur_words = []
            
            cur_words.append(word)
            num_letters += len(word)
        
        # Add the final line to the result
        res.append(" ".join(cur_words).ljust(maxWidth))
        return res