# https://leetcode.com/submissions/detail/530151628/
class Solution:
    def sumOddLengthSubarrays(self, arr):
        n=len(arr)
        sum=0
        for i in range(0,n):
            for j in range(i,n):
                if((i-j)%2==0):
                    for k in range(i,j+1):
                        sum+=arr[k]
        return sum