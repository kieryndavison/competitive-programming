class Solution:
    # Very similar to 415 add strings, only difference is mod and divide by 2 
    # instead of 10 since we are working with base 2 numbers rather than base 10
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a) - 1, len(b) - 1
        carry, sum = 0, []
        
        while i >= 0 or j >= 0 or carry:
            num1 = ord(a[i]) - ord('0') if i >= 0 else 0
            num2 = ord(b[j]) - ord('0') if j >= 0 else 0

            curSum = num1 + num2 + carry
            sum.append(str(curSum % 2))
            carry = curSum // 2
            i -= 1
            j -= 1
        
        return ''.join(sum)[::-1]
