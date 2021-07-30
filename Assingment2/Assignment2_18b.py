# https://leetcode.com/submissions/detail/530159484/
def largest(arr,n):
    max = arr[0]
    for i in range(1, n):
        if arr[i] > max:
            max = arr[i]
    return max

class Solution:
    def kidsWithCandies(candies, extraCandies):
        mx=largest(candies,len(candies))
        L=[]
        for i in range(0,len(candies)):
            if(candies[i]+extraCandies>=mx):
                L.append(1)
            else:
                L.append(0)
        return L