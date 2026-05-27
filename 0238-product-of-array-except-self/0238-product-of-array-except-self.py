"""
U:
    input = an array
    output = an array where each element is the products of all elements from the input array except self

    constraint: solve it in O(n) without using division 
        2 <= nums.length <= 1000
        -20 <= nums[i] <= 20

M: for each element, it involves information of left and information of right, use 1 array, calculate left and use that array to calculate right and multiply with 
P: 
    1. create an array/list "lst"
    2. iterate thru the nums, index i 
        3. for each index i, 
            if i-1 is out of bound 
                lst[i] = 1
            else
                lst[i] = lst[i-1] * num[i-1]
    lst now have all the information about left side 
    3. reverse iterate thru nums, index j 
        4. for each index j, 
            if j+1 is out of bound 
                right_project = 1
            else 
                right_project *= nums[j+1]
            lst[j] *= right_product 

    return lst
"""

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
        