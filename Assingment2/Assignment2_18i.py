# https://leetcode.com/submissions/detail/530448814/
class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        L=[]
        for i in range(0,len(index)):
            L.insert(index[i],nums[i])
        return L