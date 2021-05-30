class Solution:
    def reverseWords(self, s: str) -> str:
        list_string = list(s)
        list_string.reverse()
        
        self.reverseWord(list_string)
        res = self.trimSpaces(list_string)
            
        return "".join(res)
    
    def reverseWord(self, list_string):
        start = 0
        
        for i in range(len(list_string) + 1):
            if  i == len(list_string) or list_string[i] == " ":
                end = i - 1
                while start <= end:
                    list_string[start], list_string[end] = list_string[end], list_string[start],
                    start += 1
                    end -= 1
                start = i + 1
                
    def trimSpaces(self, list_string):
        l , r = 0, len(list_string) - 1
        while l < r and list_string[l] == " ": l += 1
        while l < r and list_string[r] == " ": r -= 1
        trimmed_string = list_string[l:r+1]
    
        res = [trimmed_string[0]]            
        for i in range(1, len(trimmed_string)):
            if res[-1] == " " and trimmed_string[i] == " ": continue
            res.append(trimmed_string[i])
        
        return res