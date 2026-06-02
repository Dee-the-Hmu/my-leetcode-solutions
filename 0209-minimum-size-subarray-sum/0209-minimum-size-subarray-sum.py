"""
U: 
    input: an array of + int "nums", a + int "target"
    output: the min len of a subarray whose sum is greater >= target, return 0 if none 

M: sliding window = subarray (continuous)
P: 
    1. best-min-size = len(nums)
    2. left, right = 0, 0 
        curr_sum = 0
    3. while right < len(nums)
        4. curr_sum += nums[right]
        5. while curr_sum >= target
            6. check size, if (right-left+1) < best-min-size, update best-min-size 
            7. curr_sum -= nums[left]
            8. left++
        9. else # curr_sum < target
            right += 1 
    10. return best-min-size
"""

class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        min_size = len(nums) + 1
        left, right = 0, 0 
        curr_sum = 0

        while right < len(nums):
            curr_sum += nums[right]
            
            while curr_sum >= target:
                if (right - left + 1) < min_size:
                    min_size = right - left + 1 
                curr_sum -= nums[left]
                left += 1
            
            right += 1 

        return 0 if min_size > len(nums) else min_size


        