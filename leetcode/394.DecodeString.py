class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        cur_num = 0
        cur_word = ''
        
        for char in s:
            
            # if we find a [ we are starting a new section so save the current string and multiplier
            if char == '[':
                stack.append(cur_word)
                stack.append(cur_num)
                cur_word = ''
                cur_num = 0
            
            # if we find a ] we have finished the section so compute the decoded string and add it the the current string
            elif char == ']':
                num = stack.pop()
                prev_word = stack.pop()
                cur_word = prev_word + num * cur_word
            
            # if it is a digit then it is part of the multiplier so compute it
            elif char.isdigit():
                cur_num = cur_num * 10 + int(char)
            
            # otherwise it is a letter so add it to the current string
            else:
                cur_word += char
        
        return cur_word