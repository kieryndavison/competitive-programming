from collections import defaultdict

def longestWord(text, words):
    map = defaultdict(list)
    for word in words:
        t = (word, 0)
        map[word[t[1]]].append(t)
    
    found = []
    for char in text:
        if char in map:
            for word, i in map[char]:
                i += 1
                if i == len(word):
                    found.append(word)
                else: 
                    map[word[i]].append((word, i))
            del map[char]
    
    maxWord = ""
    for word in found:
        if len(word) > len(maxWord):
            maxWord = word
    
    return maxWord

s = "abppplee"
d = ["able", "ale", "apple", "bale", "kangaroo"]
print(longestWord(s, d))