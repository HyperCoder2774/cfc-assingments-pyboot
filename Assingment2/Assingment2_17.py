# https://leetcode.com/submissions/detail/530511966/
def Repermute(One,Full,nums,state):
    if len(One)==len(nums):
        Full.append(One)
        print(One)
        return
    for i in range(0,len(nums)):
        if state[i]:
            state[i]=0
            One.append(nums[i])
            Repermute(One,Full,nums,state)
            state[i]=1
            One.remove(nums[i])
def permute(nums):
    state = []
    n = len(nums)
    for i in range(0, n):
        state.append(1)
    Full = []
    One = []
    Repermute(One, Full, nums, state)
    return
n=int(input())
nums=[]
for _ in range(0,n):
    D=int(input())
    nums.append(D)
permute(nums)
