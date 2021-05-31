class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i, j = len(num1) - 1, len(num2) - 1
        carry, total = 0, []
        
        while i >= 0 or j >= 0:
            n1 = int(num1[i]) if i >= 0 else 0
            n2 = int(num2[j]) if j >= 0 else 0

            curSum = carry + n1 + n2
            total.append(str(curSum % 10))
            carry = curSum // 10
            i -= 1
            j -= 1
        
        if carry: total.append(str(carry))
        return "".join(total)[::-1]
            