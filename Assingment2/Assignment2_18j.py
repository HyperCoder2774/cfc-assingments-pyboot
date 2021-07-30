# https://leetcode.com/submissions/detail/530456530/
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        L=[]
        n=len(prices)
        for i in range(0,n):
            mn=10000
            for j in range(i+1,n):
                if(prices[j] <= prices[i]):
                    mn=(prices[i]-prices[j])
                    break
            if(mn<prices[i]):
                L.append(mn)
            else:
                L.append(prices[i])
        return L