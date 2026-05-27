"""
U
    Input: 1-indexed array of int "numbers" (sorted)
    output: int array of [smaller index + 1, larger index + 1]
        #indices of 2 numbers that add up to a specific "target" where [smaller index, larger index]

    Condition: exactly 1 solution 
    Constraint: constant extra space O(1)

M: 2 ptrs 
plan: 
    1. left = 0, right = len(numbers) - 1
    2. while (left < right)
        3. left_val = numbers[left], right_val = numbers[right]
        4. if left_val + right_val == target
            return [left+1, right+1]
            elif left_val + right_val > target
                right -= 1 
                continue
            else: 
                left += 1 
                continue 

        return[-1,-1]
"""

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(numbers) - 1

        while(left < right):
            left_val = numbers[left]
            right_val = numbers[right]

            if left_val + right_val == target: 
                return [left+1, right+1]
            elif left_val + right_val > target: 
                right -= 1
            else: 
                left += 1 

        return [-1, -1]
        