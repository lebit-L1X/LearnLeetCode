
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #bottom up approach
        if amount == 0:
            return 0
        
        if len(coins) == 1 and coins[0] == 1:
            return amount

        amount_left = amount
        combinations = [999 for _ in range(amount+1)]

        combinations[0] = 0
        
        for i in range(1,amount+1,1):
            amount_left = i
            for j in range(len(coins)):
                amount_left = i
                amount_left -= coins[j]
                if amount_left >= 0 and combinations[amount_left]!=999 :
                    combinations[i] = min(combinations[i], combinations[amount_left]+1)
                else:
                    pass
    
    
        return combinations.pop(-1) if combinations[i] !=999 else -1
              
                
            
