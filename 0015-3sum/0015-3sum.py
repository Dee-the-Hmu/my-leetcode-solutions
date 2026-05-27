"""
U
    input: int array "nums"
    output: return all triplets (unique indices, i != j, i != k, j!= k) and num[i] + num[j] + num[k] = 0

    don't include duplicate triplets 

match: sort + iteration + 2 ptrs
plan: 
    create a list result = []
    1. iterate the nums 
    2. for each num, index i, left = current index + 1, right = len(nums) - 1)
    3. while(left < right)
        curr_val = each_num + nums[left] + nums[right]

        if curr_val == target: 
            result.append([i, left, right])
        elif curr_val > target
            right -= 1 
        else curr_val < target
            left += 1
            continue 
    4. return result

     

"""

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()

        result = [] 
        for i,num in enumerate(nums):
            left = i+1
            right = len(nums) - 1
            
            while(left < right):
                curr_val = num + nums[left] + nums[right]

                if curr_val == 0: 
                    new_lst = [nums[i], nums[left], nums[right]]
                    if new_lst not in result: 
                        result.append(new_lst)
                    left += 1
                    right -= 1 
                elif curr_val > 0: 
                    right -= 1 
                else: 
                    left += 1 
                    
        return result 

        