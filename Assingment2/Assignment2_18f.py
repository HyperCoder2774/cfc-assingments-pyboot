# https://leetcode.com/submissions/detail/530196915/
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n=len(nums)
        for i in range(0,n):
            nums[i]=nums[i]*nums[i]
        nums.sort()
        return nums