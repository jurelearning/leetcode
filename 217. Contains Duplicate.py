class Solution:
	def containDuplicate(self, nums:List[int]) -> bool:
		nums_set = set(nums)
        if len(nums) - len(nums_set) != 0:
            return true
        else:
            return false
