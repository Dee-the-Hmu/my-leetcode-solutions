class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        result = []
        lst = []
        cur_index = 0

        nums.sort()

        def backtrack(lst: List[int], cur_index: int): 
            
            #append
            result.append(lst.copy())

            #base case 
            if (cur_index == len(nums)):
                return 

            #choices 
            for i in range(cur_index, len(nums)):

                #skip when the same level has the same item 
                if i > cur_index and nums[i] == nums[i-1]:
                    continue

                #choose 
                lst.append(nums[i])

                #explore 
                backtrack(lst, i + 1)

                #undo 
                lst.pop()

        backtrack(lst, cur_index)
        return result
            