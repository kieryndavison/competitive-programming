class Solution:
    def compress(self, chars: List[str]) -> int:
        length, indexAns = 0, 0
        
        for i, char in enumerate(chars):
            length += 1
            if i == len(chars) - 1 or char != chars[i + 1]: 
                chars[indexAns] = char
                indexAns += 1

                if length > 1:
                    for digit in str(length):
                        chars[indexAns] = digit
                        indexAns += 1
                length = 0
        return indexAns