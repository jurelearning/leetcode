class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0
        l = 0
        for r in range(1, len(prices)):
            if prices[r] < prices[l]:
                l = r
            maxp = max(maxp, prices[r] - prices[l])
        return maxp        
        
        
        
#         maxp, buyp = 0, 0
#         i = 0
#         while i < len(prices):
#             buyp = prices[i]
#             for j in range(i, len(prices)):
#                 val = prices[j] - buyp
#                 if maxp < val:
#                     maxp = val
#             i += 1
#         return maxp
