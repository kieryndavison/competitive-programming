class Solution:
    # Use a state machine and at each iteration of the loop update each state based on which states can lead to it.
    def checkRecord(self, n: int) -> int:
        mod = 1000000007
        a0l0 = 1
        a0l1 = a0l2 = a1l0 = a1l1 = a1l2 = 0
        
        for _ in range(n + 1):
            new_a0l0 = (a0l0 + a0l1 + a0l2) % mod
            a0l2 = a0l1
            a0l1 = a0l0
            a0l0 = new_a0l0
            new_a1l0 = (a0l0 + a1l0 + a1l1 + a1l2) % mod
            a1l2 = a1l1
            a1l1 = a1l0
            a1l0 = new_a1l0
        
        return a1l0 % mod
