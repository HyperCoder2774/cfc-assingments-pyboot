# https://leetcode.com/submissions/detail/530192374/
def swap(i,j,L):
    L[i],L[j]=L[j],L[i]
class Solution:
    def sortArrayByParity(self, L: List[int]) -> List[int]:
        n=len(L)
        for i in range(0,n):
            if(L[i]%2):
                for j in range(i,n):
                    if(L[j]%2==0):
                        swap(i,j,L)
        return L