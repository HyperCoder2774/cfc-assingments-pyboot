# https://leetcode.com/submissions/detail/530161810/
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        n=len(nums)
        M=0
        for i in range(0,n):
            for j in range(i+1,n):
                if(nums[i]==nums[j]):
                    M=M+1
        return M