class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        balances = defaultdict(int)
        
        # Compute the balances for each person by subtracting amount if they 
        # are giving money and adding amount if they are receiving money
        for giver, receiver, amount in transactions:
            balances[giver] -= amount
            balances[receiver] += amount

        # Only include balances that are not 0 in the debt list   
        debt = []
        for _, amount in balances.items():
            if amount != 0:
                debt.append(amount)

        # dfs on the debt list
        return self.dfs(debt)
    
    def dfs(self, debt, index = 0):
        # Skip any items with value 0
        while index < len(debt) and debt[index] == 0:
            index += 1
        
        # If there are no items left with value not equal to 0 then we are done so return 0
        if index == len(debt):
            return 0
        
        # Otherwise try adding each item with j >= index + 1 and debt[j] * debt[index] < 0 (aka debt[j] has opposite sign to debt[index])
        res = float('inf')
        for j in range(index+1, len(debt)):
            if debt[j] * debt[index] < 0:
                debt[j] += debt[index]
                res = min(res, 1 + self.dfs(debt, index + 1))
                debt[j] -= debt[index] # Backtrack to try other transaction combinations
        
        return res