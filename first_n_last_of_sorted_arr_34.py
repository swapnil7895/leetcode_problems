

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1,-1]
        start_ind = nums.index(target)
        last_ind = start_ind
#        for i in range( start_ind, len(nums) , -1):
        for i in range( len(nums)-1, start_ind ,-1):    
            if nums[i] == target:
                last_ind= i
                break
        return [start_ind, last_ind]

