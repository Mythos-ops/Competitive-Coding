class Solution:
    def maxSubarraySumCircular(self,nums:List[int])->int:
        total=nums[0]
        maxSum=nums[0]
        minSum=nums[0]
        curMax=nums[0]
        curMin=nums[0]

        for i in range(1,len(nums)):
            x=nums[i]
            curMax=max(x,curMax+x)
            maxSum=max(maxSum,curMax)
            curMin=min(x,curMin+x)
            minSum=min(minSum,curMin)
            total+=x

        if maxSum<0:
            return maxSum

        return max(maxSum,total-minSum)