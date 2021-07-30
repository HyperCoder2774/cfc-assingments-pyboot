# https://leetcode.com/submissions/detail/530520221/
def maxProfit(self, prices: List[int]) -> int:
    mn = 1000000
    profit = 0
    for i in range(0, len(prices)):
        if mn > prices[i]:
            mn = prices[i]
        elif prices[i] - mn > profit:
            profit = prices[i] - mn
    return profit