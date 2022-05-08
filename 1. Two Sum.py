class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        pairMap={}
        for i in range(len(nums)):
            firstval = target - nums[i]
            if firstval in pairMap:
                return [pairMap[firstval], i]
            pairMap[nums[i]] = i
            
            
#             for j in range(len(nums)):
#                 if j != i:
#                     if nums[j] == firstval:
#                         return [i, j] 