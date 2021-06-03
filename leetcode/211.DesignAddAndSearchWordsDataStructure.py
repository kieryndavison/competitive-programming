class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False
    
    # here we have to recursively check each possible character that we could replace '.' 
    # with, if any of them form a word then we return true, otherwise we return false
    def findWord(self, word):
        cur = self
        
        for i, char in enumerate(word):
            if char in cur.children:
                cur = cur.children[char]
            
            elif char == '.':
                for child in cur.children.values():
                    if child.findWord(word[i+1:]):
                        return True

                return False

            else: return False
        
        return cur.is_word 
        

class WordDictionary:

    # typical trie init and insert functions
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        
        for char in word:
            cur = cur.children[char]
        
        cur.is_word = True

    # this is the interesting one
    def search(self, word: str) -> bool:
        return self.root.findWord(word)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)