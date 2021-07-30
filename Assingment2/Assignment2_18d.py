# https://leetcode.com/submissions/detail/530185237/
class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        n=len(arr)
        K=0
        for i in range(0,n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if abs(arr[i]-arr[j])<=a and abs(arr[j]-arr[k])<=b and abs(arr[i]-arr[k])<=c:
                        K+=1
        return K