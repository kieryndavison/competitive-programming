# Define a class for the nodes in the trie which contains its 
# children and whether it is the last letter in a wordd
class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False

class Trie:

    # Create a root node for our trie
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    # Add in all the characters in the word to the trie if they dont already exist
    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self.root
        for char in word:
            # adds char to dictionary with default value or else updates 
            # current to point to the node with a value of char
            cur = cur.children[char] 
            
        cur.is_word = True

    # If any character in the word is not in the trie or the final character is 
    # not the last character in a word then return false
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur = self.root
        for char in word:
            cur = cur.children.get(char)
            if not cur:
                return False
            
        return cur.is_word
    
    # Similar to search but the last character does not have to be a word
    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur = self.root
        for char in prefix:
            cur = cur.children.get(char)
            if not cur:
                return False
            
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)