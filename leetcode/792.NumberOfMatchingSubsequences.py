# Solution 1 using iterator to keep track of the current letter
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        cur_letters = defaultdict(list)
        for it in map(iter, words):
            cur_letters[next(it)].append(it)
                
        for char in s:
            for it in cur_letters.pop(char, ()):
                 cur_letters[next(it, None)].append(it)
        
        return len(cur_letters[None])

# Solution 2 add a ' ' so that we can account for the empty string
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        cur_letters = defaultdict(list, {' ': map(iter, words)})
        
        for char in ' ' + s:
            for it in cur_letters.pop(char, ()):
                cur_letters[next(it, None)].append(it)
        
        return len(cur_letters[None])