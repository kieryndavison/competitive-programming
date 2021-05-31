class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # convert string to list since strings are immuatble
        listChars = list(s)
        stack = []
        
        for i, char in enumerate(listChars):

            # if we find a ')' remove its matching '(' from the stack or else remove it from the list
            if char == ')':
                if stack: stack.pop()
                else: listChars[i] = ''
            
            # if we find a '(' add its index to the stack
            elif char == '(': 
                stack.append(i)
        
        # if we have any '(' left over at the end remove them from the list
        while stack:
            listChars[stack.pop()] = ''
        
        # return the string created by joining together all the characters in the list
        return "".join(listChars)