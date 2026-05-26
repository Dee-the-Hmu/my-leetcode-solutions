class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [] #lst

        for i in range(len(nums)):
            if i-1 < 0: 
                result.append(1)
            else: 
                result.append(result[i-1] * nums[i-1])

        for j in range(len(nums) -1, -1, -1):
            if j + 1 >= len(nums):
                right_product = 1
            else: 
                right_product *= nums[j+1]

            result[j] *= right_product 

        return result
        