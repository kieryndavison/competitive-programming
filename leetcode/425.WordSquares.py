class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        trie = defaultdict(set)
        n = len(words[0])
        
        for word in words:
            for i in range(len(word)):
                trie[word[:i]].add(word)
        
        def buildSquares(square, i):
            if i == n:
                squares.append(square)
                return
            
            prefix = ""
            for j in range(0, i):
                prefix += square[j][i]
            
            for word in trie[prefix]:
                buildSquares(square + [word], i+1)
        
        squares = []
        buildSquares([], 0)
        return squares