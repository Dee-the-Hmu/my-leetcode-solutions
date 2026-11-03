class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = []
        i = 0
        lst = []

        def backtracking(lst, i):
            #base case
            if i == len(nums):
                result.append(lst.copy())
                return

            #no condition
            #choose
            lst.append(nums[i])

            #explore
            backtracking(lst, i + 1)

            #undo 
            lst.pop()

            #2nd explore (subset = include current element, not include)
            backtracking(lst, i + 1)

        backtracking(lst, i)
        return result
        